import dask
import xarray as xr
import numpy as np
import pandas as pd  # <--- NEW: Needed for timestamp parsing
from dask.distributed import Client, LocalCluster
from pathlib import Path
import grid_utils

# --- Configuration ---
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "phase2" / "data" 
OUTPUT_DIR = BASE_DIR / "phase2" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ROI (Same as Phase 1)
LAT_SLICE = slice(20, 40)
LON_SLICE = slice(-160, -140)

# Ice Proj String (Static)
ICE_PROJ_STR = "+proj=stere +lat_0=90 +lat_ts=70 +lon_0=-45 +k=1 +x_0=0 +y_0=0 +a=6378273 +b=6356889.449 +units=m +no_defs"

def preprocess_chl(ds):
    """
    Injects a 'time' dimension into NASA VIIRS files based on attributes.
    Required because L3m files are 2D (lat/lon) by default.
    """
    # 1. Extract time from global attributes
    # NASA standard attribute: 'time_coverage_start' (e.g., '2020-01-01T00:00:00Z')
    if 'time_coverage_start' in ds.attrs:
        t_str = ds.attrs['time_coverage_start']
        t_obj = pd.to_datetime(t_str).tz_localize(None)
        
        # 2. Add the dimension
        # expand_dims creates the 'time' coord and dimension of length 1
        ds = ds.expand_dims(time=[t_obj])
        
    return ds

def main():
    # 1. Start Dask Cluster
    cluster = LocalCluster()
    client = Client(cluster)
    print(f"--- Dask Cluster Running ---")
    print(f"Dashboard: {client.dashboard_link}")
    print(f"Workers: {len(client.scheduler_info()['workers'])}")

    print("\n1. Lazy Loading Data...")
    
    # SST (Already has time dim, just needs chunking)
    ds_sst = xr.open_mfdataset(
        str(DATA_DIR / "oisst*.nc"), 
        combine="by_coords", 
        parallel=False, 
        chunks={"time": 1, "lat": -1, "lon": -1}
    )
    
    # Chlorophyll (NEEDS PREPROCESSOR)
    # We add 'preprocess=preprocess_chl' here
    ds_chl = xr.open_mfdataset(
        str(DATA_DIR / "JPSS1*.nc"), 
        combine="by_coords", 
        parallel=False,
        preprocess=preprocess_chl,  # <--- The Magic Fix
        chunks={"time": 1, "lat": -1, "lon": -1}
    )

    # Sea Ice (Already has time dim)
    ds_ice = xr.open_mfdataset(
        str(DATA_DIR / "sic*.nc"), 
        combine="by_coords", 
        parallel=False,
        chunks={"time": 1, "y": -1, "x": -1}
    )

    print("   Datasets linked (Lazy). No data read yet.")

    # 3. Preprocess Coordinates (Lazy)
    # Normalize SST Lon
    ds_sst.coords['lon'] = (ds_sst.coords['lon'] + 180) % 360 - 180
    ds_sst = ds_sst.sortby(['lon', 'lat'])
    
    # Slice SST to ROI
    sst_subset = ds_sst.sel(lat=LAT_SLICE, lon=LON_SLICE)
    
    # Drop scalar 'time' conflicts
    sst_subset = sst_subset.drop_vars("zlev", errors="ignore")

    print(f"   Target Grid Shape (Virtual): {sst_subset['sst'].shape}")
    # --- NEW: FORCE TIME ALIGNMENT ---
    # Resample all datasets to Daily ('1D') frequency.
    # .mean() is safe here because we only have 1 data point per day anyway.
    # This snaps '12:00:00' and '00:00:00' both to '2020-01-01'
    sst_subset = sst_subset.resample(time='1D').mean()
    ds_chl = ds_chl.resample(time='1D').mean()
    ds_ice = ds_ice.resample(time='1D').mean()
    # 4. Construct the Graph
    print("\n2. Building Computation Graph...")
    
    # A. Chlorophyll Regridding
    # Now ds_chl has a 'time' dimension, so interp_like works across time!
    chl_regridded = ds_chl['chlor_a'].interp_like(sst_subset, method='linear')
    
    # B. Sea Ice Projection
    target_x, target_y = grid_utils.precompute_ice_indices(
        sst_subset.lat.values, 
        sst_subset.lon.values, 
        ICE_PROJ_STR
    )
    
    ice_regridded = ds_ice['cdr_seaice_conc'].interp(
        x=target_x, 
        y=target_y, 
        method="nearest"
    )

    # 5. Merge
    ds_merged = xr.Dataset({
        'sst': sst_subset['sst'],
        'chlor_a': chl_regridded,
        'ice_conc': ice_regridded
    })
    ds_merged = ds_merged.chunk({'time': -1, 'lat': -1, 'lon': -1})
    print(f"   Merged Dataset (Virtual): {ds_merged}")
    
    # 6. PRODUCTION: Write to Zarr
    # This triggers the full computation for all 31 days
    zarr_path = OUTPUT_DIR / "ocean_analysis_jan2020.zarr"
    print(f"\n3. Writing full dataset to {zarr_path}...")
    
    # Delete existing store if it exists (Zarr requires clean path)
    if zarr_path.exists():
        import shutil
        shutil.rmtree(zarr_path)
    
    # The progress bar requires 'dask' to be installed with 'diagnostics' 
    # or we can just trust the dashboard.
    # compute=True forces execution immediately.
    ds_merged.to_zarr(zarr_path, mode='w', compute=True)
    
    print("   Success! Zarr store created.")
    
    # 7. Verification Read
    print("4. Verifying Zarr Store...")
    ds_final = xr.open_zarr(zarr_path)
    print(ds_final)
    input("Press Enter to shutdown the cluster...") 
    client.close()

if __name__ == "__main__":
    main()
