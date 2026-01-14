# **PHASE 4 — Spark ML Pipeline (Full UC San Diego–Aligned Step‑by‑Step Guide)**

Now that you have completed:
- Phase 1 (local feasibility),
- Phase 2 (Dask prototype),
- Phase 3 (SDSC preprocessing → Parquet output),

you are ready to build the **Spark ML** pipeline using the cleaned, partitioned Parquet dataset stored on SDSC or DSMLP.

Spark is directly relevant to UCSD’s data‑science and ML curriculum, which emphasizes scalable analytics using Spark, its ML capabilities, and data‑flow style operations for cleaning, feature engineering, and large‑scale modeling

This phase builds your machine‑learning pipeline exactly in that style.

────────────────────────────────────────
## **Step 1 — Configure Spark Environment**

### Where to run Spark at UC San Diego:
You have two practical environments:

• **DSMLP (Data Science & Machine Learning Platform)**: supports complex customizations including Spark clusters, ML workflows, and distributed jobs 
• **SDSC HPC**: if Spark is installed or run via containers/modules.

How to proceed:
- Start a Spark session with sufficient memory and cores.
- Point Spark to the directory containing your cleaned Parquet files.
- Ensure Python environment includes pyspark and your ML libraries.

────────────────────────────────────────
## **Step 2 — Load the Parquet Dataset into Spark**

Goal: Read the multi‑file, partitioned Parquet dataset produced in Phase 3.

How to proceed:
- Use Spark’s `read.parquet()` to load all partitions at once.
- Verify schema correctness (lat, lon, time, sst, chlor_a, sea_ice_conc, derived features).
- Cache the dataset in memory if feasible.

────────────────────────────────────────
## **Step 3 — Build Spark Feature‑Engineering Pipelines**

Goal: Convert raw columns into ML‑ready features at scale.

How to proceed:
- Use Spark Transformers for:
  - handling missing values,
  - normalization,
  - vector assembly,
  - categorical encodings (if any),
  - automatic feature scaling,
  - log‑transforming chlorophyll if needed.
- Spark Pipelines ensure transformations are consistent across train/test.

────────────────────────────────────────
## **Step 4 — Train ML Models Using Spark MLlib**

Goal: Train three ML models at scale.

### **Model A — K‑Means (ecological zones)**
- Use `KMeans` from MLlib.
- Select `k` using silhouette score.
- Fit the model on SST + chlorophyll + latitude features.
- Map cluster labels back onto coordinates.

### **Model B — Random Forest Classifier (bloom prediction)**
- Define target bloom class (e.g., chlorophyll > percentile threshold).
- Use `RandomForestClassifier`.
- Examine feature importances.

### **Model C — Gradient‑Boosted Trees or XGBoost‑style Regression**
- Spark MLlib includes GBTRegressor.
- Predict chlorophyll values using SST anomalies, DOY, latitude, etc.
- Evaluate RMSE and $R^2$.

────────────────────────────────────────
## **Step 5 — Perform Model Evaluation at Scale**

Goal: Obtain metrics that validate your models across large datasets.

How to proceed:
- Use Spark’s evaluation tools:
  - BinaryClassificationEvaluator
  - RegressionEvaluator
  - ClusteringEvaluator
- Compute metrics per region or per partition if needed.

────────────────────────────────────────
## **Step 6 — Run Spatial Post‑Processing**

Goal: Apply your trained Spark models to entire global datasets.

How to proceed:
- Use Spark inference to generate:
  - global cluster labels (from K‑Means),
  - bloom predictions,
  - chlorophyll predictions.
- Collect results in manageable batches.
- Export predictions to Parquet.

────────────────────────────────────────
## **Step 7 — Visualize Model Outputs (Locally or on DSMLP)**

Goal: Create interpretable maps and plots for your final report.

How to proceed:
- Export Spark results to smaller Parquet files.
- Load them locally (Python or DSMLP Jupyter).
- Create:
  - global chlorophyll prediction maps,  
  - bloom classification maps,  
  - cluster‑label maps,  
  - correlation residual plots.

────────────────────────────────────────
## **Step 8 — Document Spark ML Pipeline for Final README**

Goal: Produce complete documentation for Milestone 4.

How to proceed:
- Describe Spark environment setup.
- Explain pipeline components:
  - ingestion,
  - transformation,
  - model training,
  - evaluation,
  - visualization.
- Include narrative explanations and code blocks in the README (but code not required here).
- Highlight reproducibility and scalability.

────────────────────────────────────────

# **Summary**
Phase 4 completes your full big‑data ML lifecycle using Spark, incorporating core principles from UCSD’s scalable analytics and machine‑learning ecosystems 
You now have:

- scalable Spark ingestion of your SDSC‑processed dataset,  
- reusable Spark pipelines for feature engineering,  
- distributed ML models (K‑Means, RF, GBT),  
- full evaluation and visualization workflow,  
- documentation ready for your final submission.  

This brings your project fully into UC San Diego’s expected standards for data‑intensive and ML‑driven workflows.

────────────────────────────────────────

