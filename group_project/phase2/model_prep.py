import xarray as xr
import pandas as pd
import numpy as np
from pathlib import Path

# --- Config ---
BASE_DIR = Path(__file__).parent.parent
ZARR_PATH = BASE_DIR / "phase2" / "output" / "ocean_analysis_jan2020.zarr"

def main():
    print(f"--- Loading Zarr Cube from {ZARR_PATH.name} ---")
    
    # 1. Load the Cube
    ds = xr.open_zarr(ZARR_PATH)
    print(f"Cube Shape: {ds['sst'].shape} (Time, Lat, Lon)")
    
    # 2. Stack Dimensions (The Flattening)
    print("\n1. Flattening the Cube...")
    ds_flat = ds.stack(sample=("time", "lat", "lon"))
    print(f"Flattened Shape: {ds_flat['sst'].shape} (Samples,)")
    
    # 3. Convert to DataFrame (The Table)
    print("\n2. Converting to Pandas Table...")
    df = ds_flat.to_dataframe().reset_index()
    
    # Cleanup columns
    df_model = df[['time', 'lat', 'lon', 'sst', 'ice_conc', 'chlor_a']]
    print(f"Raw Table Size: {len(df_model)} rows")

    # 4. Drop Missing Data (The Reality Check)
    print("\n3. Cleaning Missing Data (Clouds/Land)...")
    
    # --- THE CRITICAL FIX ---
    # In the subtropics (Hawaii), Sea Ice is NaN. We must fill it with 0.0.
    # Otherwise, dropna() removes the entire ocean.
    df_model['ice_conc'] = df_model['ice_conc'].fillna(0.0)
    
    # Now we only drop rows where SST or Chlorophyll are genuinely missing
    df_clean = df_model.dropna()
    
    print(f"Clean Table Size: {len(df_clean)} rows")
    print(f"Data Retention: {(len(df_clean) / len(df_model)) * 100:.2f}%")
    
    if len(df_clean) == 0:
        print("\n[WARNING] Still 0 rows? Then Chlorophyll is your issue (100% Cloud Cover?).")
    else:
        print("\nSUCCESS: This is your Training Set!")
        print(df_clean.head())
        
        # Save for Scikit-Learn/PySpark
        # It saves to phase3/training_data.parquet
        save_path = BASE_DIR / "phase3" / "training_data.parquet"
        save_path.parent.mkdir(parents=True, exist_ok=True)
        df_clean.to_parquet(save_path)
        print(f"\nSaved training data to {save_path}")

if __name__ == "__main__":
    main()
