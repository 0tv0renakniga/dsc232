import xarray as xr
import numpy as np
from pathlib import Path

# Path to your output
ZARR_PATH = Path("output/ocean_analysis_jan2020.zarr")

def main():
    print(f"Inspecting: {ZARR_PATH}")
    
    # 1. Open the Store
    try:
        ds = xr.open_zarr(ZARR_PATH)
    except Exception as e:
        print(f"FATAL: Could not open Zarr store. {e}")
        return

    # 2. Check SST Data
    print("\n--- Variable Check: SST ---")
    sst = ds['sst']
    print(f"Shape: {sst.shape}")
    
    # Load just one pixel time-series to check for real values
    # (Avoid loading the whole thing to save memory)
    sample_pixel = sst.isel(lat=40, lon=40).values
    
    print(f"Sample Time Series (Center Pixel):")
    print(sample_pixel)
    
    # Check for complete emptiness
    if np.isnan(sample_pixel).all():
        print("\n[WARNING] Sample pixel is all NaN. This might be bad (or just land/cloud).")
        # Try finding ANY valid value
        print("Scanning for ANY valid value (this might take a second)...")
        valid_count = sst.notnull().sum().compute()
        print(f"Total Valid SST Pixels in dataset: {valid_count.item()}")
        
        if valid_count == 0:
            print("❌ FAIL: The SST variable is empty. The write was cancelled.")
        else:
            print("✅ PASS: Data exists (just hit a bad pixel initially).")
    else:
        print("✅ PASS: Real data detected.")

if __name__ == "__main__":
    main()
