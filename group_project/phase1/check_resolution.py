import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# --- Configuration ---
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
SST_FILE = DATA_DIR / "oisst-avhrr-v02r01.20200101.nc"
CHL_FILE = DATA_DIR / "JPSS1_VIIRS.20200101_20200108.L3m.8D.CHL.chlor_a.4km.nc"

# ROI: North Pacific
# Note: Using float slices ensures xarray selects the range inclusive
LAT_SLICE = slice(40, 20)  # OISST lat is often high-to-low or low-to-high, we handle sorting below
LON_SLICE = slice(-160, -140)

def normalize_sst(ds):
    """
    Converts OISST longitude from (0, 360) to (-180, 180) to match VIIRS.
    Sorts lat/lon to ensure slicing works predictably.
    """
    print("   -> Normalizing SST Longitude to -180/180...")
    # Adjust lon coordinates
    ds.coords['lon'] = (ds.coords['lon'] + 180) % 360 - 180
    
    # Sort to fix any ordering issues after wrap-around
    ds = ds.sortby(['lon', 'lat'])
    return ds

def main():
    print("--- Phase 1: Coordinate Alignment & Inspection ---")
    
    # 1. Load Data
    print("1. Loading datasets...")
    try:
        ds_sst = xr.open_dataset(SST_FILE)
        ds_chl = xr.open_dataset(CHL_FILE)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    # 2. Preprocess SST
    ds_sst = normalize_sst(ds_sst)

    # 3. Subset Region (North Pacific)
    print(f"2. Subsetting to ROI: Lat {LAT_SLICE}, Lon {LON_SLICE}")
    
    # Handle slice direction (xarray requires slice(min, max) if index is increasing)
    # We simply select using the user-defined bounds
    try:
        sst_subset = ds_sst.sel(lat=slice(20, 40), lon=slice(-160, -140))
        chl_subset = ds_chl.sel(lat=slice(40, 20), lon=slice(-160, -140)) # VIIRS lat is often 90 -> -90
        
        print(f"   SST Subset Shape: {sst_subset.sst.shape}")
        print(f"   CHL Subset Shape: {chl_subset.chlor_a.shape}")
    except Exception as e:
        print(f"   Slicing failed: {e}")
        print("   Check your coordinate sort order!")
        return

    # 4. Generate Milestone 2 Sanity Plot
    print("3. Generating comparison plots...")
    fig, axes = plt.subplots(1, 2, figsize=(15, 6), constrained_layout=True)

    # SST Plot
    # Squeeze out time/zlev dims for plotting
    sst_data = sst_subset['sst'].isel(time=0, zlev=0)
    sst_data.plot(ax=axes[0], cmap='RdBu_r', cbar_kwargs={'label': 'SST (°C)'})
    axes[0].set_title(f"SST (OISST) \nRes: 0.25°")

    # Chlorophyll Plot
    # Use log normalization for biology
    from matplotlib.colors import LogNorm
    chl_subset['chlor_a'].plot(ax=axes[1], cmap='viridis', norm=LogNorm(vmin=0.01, vmax=5))
    axes[1].set_title(f"Chlorophyll-a (VIIRS) \nRes: 4km")

    # Add gridlines to verify geospatial alignment
    for ax in axes:
        ax.grid(True, linestyle='--', alpha=0.5)

    save_path = BASE_DIR / "milestone2_sanity_check.png"
    plt.savefig(save_path)
    print(f"   Saved plot to {save_path}")

if __name__ == "__main__":
    main()
