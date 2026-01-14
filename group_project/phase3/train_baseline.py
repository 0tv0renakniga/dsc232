import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
from pathlib import Path

# --- Config ---
BASE_DIR = Path(__file__).parent.parent
DATA_PATH = BASE_DIR / "phase3" / "training_data.parquet"
MODEL_PATH = BASE_DIR / "phase3" / "baseline_model.pkl"

def main():
    print(f"--- Phase 3: Baseline Model Training ---")
    
    # 1. Load Data
    if not DATA_PATH.exists():
        print(f"❌ Error: Data not found at {DATA_PATH}")
        return
        
    print(f"1. Loading {DATA_PATH.name}...")
    df = pd.read_parquet(DATA_PATH)
    
    # 2. Feature Engineering (The Basics)
    # We want to predict 'chlor_a' using Physics and Location
    feature_cols = ['sst', 'ice_conc', 'lat', 'lon']
    target_col = 'chlor_a'
    
    X = df[feature_cols]
    y = df[target_col]
    
    print(f"   Features: {feature_cols}")
    print(f"   Target: {target_col}")
    print(f"   Total Samples: {len(df)}")

    # 3. Train/Test Split
    # We hide 20% of the data to test if the model actually learned anything
    print("\n2. Splitting Data (80% Train / 20% Test)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"   Training Set: {len(X_train)} rows")
    print(f"   Test Set: {len(X_test)} rows")

    # 4. Train Model
    print("\n3. Training Random Forest (this may take a moment)...")
    # n_jobs=-1 uses all your CPU cores to speed it up
    rf = RandomForestRegressor(n_estimators=50, max_depth=10, n_jobs=-1, random_state=42)
    rf.fit(X_train, y_train)

    # 5. Evaluate
    print("\n4. Evaluating Performance...")
    y_pred = rf.predict(X_test)
    
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    
    print(f"   -----------------------------")
    print(f"   RMSE: {rmse:.4f} (Lower is better)")
    print(f"   R²:   {r2:.4f}   (1.0 is perfect)")
    print(f"   -----------------------------")

    # 6. Feature Importance (Sanity Check)
    # What did the model actually use?
    print("\n5. Feature Importance:")
    for name, importance in zip(feature_cols, rf.feature_importances_):
        print(f"   {name}: {importance:.4f}")

    # 7. Save
    joblib.dump(rf, MODEL_PATH)
    print(f"\n✅ Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    main()
