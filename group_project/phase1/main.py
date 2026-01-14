import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyproj
from pathlib import Path

# --- Configuration ---
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# Files
SST_FILE = DATA_DIR / "oisst-avhrr-v02r01.20200101.nc"
CHL_FILE = DATA_DIR / "JPSS1_VIIRS.20200101_20200108.L3m.8D.CHL.chlor_a.4km.nc"
ICE_FILE = DATA_DIR / "sic_psn25_20200101_F17_v05r00.nc"

# ROI: North Pacific
LAT_SLICE = slice(20, 40) 
LON_SLICE = slice(-160, -140)

# NSIDC Polar Stereographic PROJ4 String (From your ncdump)
# Note: Critical parameters are lat_0, lat_ts, lon_0, and the ellipsoid (a/b)
ICE_PROJ_STR = "+proj=stere +lat_0=90 +lat_ts=70 +lon_0=-45 +k=1 +x_0=0 +y_0=0 +a=6378273 +b=6356889.449 +units=m +no_defs"

def normalize_sst(ds):
    """Wraps SST longitude to -180/180 and sorts coordinates."""
    ds.coords['lon'] = (ds.coords['lon'] + 180) % 360 - 180
    ds = ds.sortby(['lon', 'lat'])
    return ds

def regrid_sea_ice(ds_ice, target_lat, target_lon):
    """
    Reprojects Sea Ice data (x/y) onto the Target Grid (lat/lon).
    """
    print("   -> Reprojecting Sea Ice to Target Grid...")
    
    # 1. Create a Transformer: Lat/Lon (EPSG:4326) -> Polar Stereo
    # always_xy=True ensures input order is (lon, lat)
    transformer = pyproj.Transformer.from_crs("EPSG:4326", ICE_PROJ_STR, always_xy=True)

    # 2. Create a meshgrid of the TARGET coordinates (SST Grid)
    # We need to look up every SST pixel location in the Ice dataset
    lon_grid, lat_grid = np.meshgrid(target_lon, target_lat)
    
    # 3. Transform target Lat/Lon to Ice X/Y
    target_x, target_y = transformer.transform(lon_grid, lat_grid)
    
    # 4. Interpolate
    # We create xarray DataArrays for the coordinates to allow vectorized interpolation
    x_da = xr.DataArray(target_x, dims=("lat", "lon"))
    y_da = xr.DataArray(target_y, dims=("lat", "lon"))
    
    # Use nearest neighbor since Ice is categorical/mask-heavy, 
    # but linear is okay for concentration if careful. 
    # We stick to nearest to avoid creating fake ice at edges.
    ds_ice_regridded = ds_ice.interp(x=x_da, y=y_da, method="nearest")
    
    return ds_ice_regridded

def main():
    print("--- Phase 1: Data Fusion & DataFrame Creation ---")
    
    # 1. Load Data
    ds_sst = xr.open_dataset(SST_FILE)
    ds_chl = xr.open_dataset(CHL_FILE)
    ds_ice = xr.open_dataset(ICE_FILE)

    # 2. Prepare Base Grid (SST)
    ds_sst = normalize_sst(ds_sst)
    ds_sst = ds_sst.sortby('lat')
    
    # Create SST Subset (Master Grid)
    # We drop 'time' and 'zlev' immediately to prevent merge conflicts later
    sst_subset = ds_sst.sel(lat=LAT_SLICE, lon=LON_SLICE).isel(time=0, zlev=0)
    sst_da = sst_subset['sst'].drop_vars(['time', 'zlev'], errors='ignore')
    
    print(f"1. Master Grid (SST) Shape: {sst_da.shape}")

    # 3. Process Chlorophyll
    print("2. Processing Chlorophyll...")
    # Interp onto SST grid
    # We explicitly drop 'time' if it was carried over or exists in CHL
    chl_regridded = ds_chl['chlor_a'].interp_like(sst_subset, method='linear')
    chl_da = chl_regridded.drop_vars('time', errors='ignore')

    # 4. Process Sea Ice
    print("3. Processing Sea Ice...")
    ice_var = ds_ice['cdr_seaice_conc'].isel(time=0)
    ice_regridded = regrid_sea_ice(ice_var, sst_subset.lat, sst_subset.lon)
    ice_da = ice_regridded.drop_vars('time', errors='ignore')

    # 5. Merge into one Dataset
    print("4. Merging datasets...")
    # Now all inputs are clean 2D arrays (lat, lon) with no conflicting scalar coords
    merged = xr.Dataset({
        'sst': sst_da,
        'chlor_a': chl_da,
        'ice_conc': ice_da
    })

    # 6. Sanity Check Plot
    fig, ax = plt.subplots(1, 1, figsize=(6, 5))
    merged['sst'].plot(ax=ax, alpha=0.6, cmap='Reds', label='SST')
    high_chl = merged['chlor_a'].where(merged['chlor_a'] > 0.2)
    if not high_chl.isnull().all():
        high_chl.plot(ax=ax, cmap='viridis', add_colorbar=False, alpha=0.5)
    ax.set_title("SST with Chlorophyll Overlay (Regridded)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "milestone2_fusion_check.png")
    print("   -> Saved fusion plot.")

    # 7. Export to DataFrame
    print("5. Exporting to DataFrame...")
    df = merged.to_dataframe().reset_index()
    
    # Clean up (Drop rows where SST is NaN, usually land)
    df_clean = df.dropna(subset=['sst'])
    
    print(f"   Final DataFrame Shape: {df_clean.shape}")
    print(df_clean.head())
    
    output_path = OUTPUT_DIR / "phase1_dataset.parquet"
    df_clean.to_parquet(output_path)
    print(f"   -> Saved data to {output_path}")

if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
