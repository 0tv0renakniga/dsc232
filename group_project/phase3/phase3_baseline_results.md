# Phase 3 Roadmap: Machine Learning & Analysis

**Goal:** Predict Ocean Chlorophyll (Biology) using SST (Physics) and Location.

## 1. Baseline Model (Completed)
- [x] Load Parquet data.
- [x] Train Random Forest Regressor (Default parameters).
- [x] **Result:** R² = 0.817.
- [x] **Key Finding:** SST (61%) and Latitude (29%) drives the prediction.

## 2. Model Improvement (Next Steps)
- [ ] **Imputation:** Can we recover the "Cloudy" pixels?
    * *Idea:* Train a model to predict Chlorophyll from SST, then use it to fill gaps.
- [ ] **Feature Engineering:**
    * *Time Lags:* Does the SST *yesterday* predict the bloom *today*? (Algae takes time to grow).
    * *Anomalies:* Instead of raw Temp, use "Deviation from Normal."
- [ ] **Algorithm Comparison:**
    * Try XGBoost or LightGBM (often faster/better than Random Forest).
    * Try a simple Neural Network (PyTorch) if time permits.

## 3. Evaluation & Visualization
- [ ] **Error Map:** Plot the residuals (Predicted - Actual) on a map. Are we failing in specific regions (e.g., near the coast)?
- [ ] **Time Series Plot:** Pick one pixel and plot the predicted vs. actual time series for January.
