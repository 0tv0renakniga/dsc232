# Project: Machine Learning Analysis of Temperature–Biology Coupling in Global Oceans

## Milestone 1
- **Description: Milestone 1...**

---

### Stages
#### Stage 0: Project Initilazation
- **Goal: prepare the conceptual foundation and technical plan.**
    - 0.1 Finalize scientific framing
        - Define your overarching question:
        - “How strongly does ocean temperature control biological productivity, and can we predict blooms and marine heatwave impacts using ML?”
        - Clarify sub‑questions (clustering, bloom prediction, regression, correlation).
        - Write this down in a shared document for your team.
    - 0.2 Select geographic and temporal scope for feasibility tests
        - Pick one region (e.g., North Pacific) for Phase 1.
        - Pick 1–2 months of data for initial tests.
        - Identify exact datasets and URLs.
    - 0.3 Create project structure
        - GitHub repo with these folders:
        - data_raw, data_processed, notebooks, src, docs
        - Add README skeleton and contribution guidelines.

---

#### Stage 1: Abstract, Group, Data Description
- **Goal: Produce a polished abstract and statement of work.**
    - 1.1 Draft short dataset descriptions
        - Identify:
        - SST dataset (source, variable, resolution, time period)
        - Chlorophyll dataset
        - Sea ice dataset
        - Note file types (NetCDF/HDF5) and typical file sizes.
    - 1.2 Describe project novelty
        - State that no overlapping projects exist in class (important for approval).
        - Emphasize combination of SST + chlorophyll + ice.
    - 1.3 Draft 1‑paragraph abstract
        - Include:
            - Scientific motivation
            - Datasets
            - Planned ML methods
            - Expected insights
            - Why Spark/HPC is necessary
    - 1.4 Submit via Gradescope

#### Stage 2: Local Feasibility Phase 1 (Polars + 1 Region)
- **Goal: “Quick and dirty” exploration to help your team see the dataset and verify feasibility.**
    - 2.1 Download small dataset slice
        - Choose one region (e.g., lat 20–40°, lon 150–200°).
        - Download 1–2 months of SST and chlorophyll.
        - Save in local directory.
    - 2.2 Inspect raw NetCDF/HDF5 files
        - Open files using xarray.
        - Print dimensions, variables, coordinates.
        - Check time stamps align (they won’t — this is part of your feasibility finding).
            - what do papers say? 
            - look for existing info 
    - 2.3 Chunk data for Polars
        - Convert xarray → pandas/Polars by flattening to a tidy DataFrame:
            - columns: [lat, lon, time, SST, chlorophyll]
        - Use Polars to check:
            - data types
            - missing values
            - sanity checks (min/max ranges)
            - row counts
    - 2.4 Produce basic visualizations
        - 2D map of SST
        - 2D map of chlorophyll
        - Scatterplot SST vs chlorophyll
    - 2.5 Document feasibility
        - You answer the question: “Is this data workable? Are patterns visible?”
        - Save plots for Milestone 2.

#### Stage 3: Local Feasibility Phase 2 (Dask + partial pipeline)
- **Goal: Build a medium-scale prototype that mirrors future SDSC pipeline.**
    - 3.1 Expand dataset
        - Increase to 3–6 months
        - Add multiple regions
        - Download SST + chlorophyll + sea ice
    - 3.2 Build preprocessing workflow using xarray + Dask
        - Sub-steps:
            - 3.2.1 Spatial alignment
                - Regrid chlorophyll (4 km) → SST grid (0.25°)
                - Use xarray’s .coarsen() or .interp()
                - Validate: map-grid match and dimension equality.
            - 3.2.2 Temporal alignment
                - SST daily
                - Chlorophyll 8‑day
                - Tasks:
                    - Align chlorophyll to nearest SST date
                    - Option: rolling mean on SST to match 8‑day composite
                    - Ensure time dimension matches exactly.
            - 3.2.3 Compute features
                - Include both raw and derived:
                    - SST raw
                    - SST anomaly relative to local climatology
                    - Day-of-year
                    - Latitude (continuous)
                    - Region ID / pixel ID
    - 3.3 Convert to tidy format
        - Flatten into DataFrame
        - Convert to parquet (Spark-ready)
        - Validate:
            - files readable
            - columns correct
            - no NaN explosions
    - 3.4 Prototype models locally
        - Note: This is ONLY for checking feasibility; not final models.
        - Run a tiny K-Means on a small sample
        - Train a tiny Random Forest
        - Make a dummy correlation map
        - Purpose:
            - Does the pipeline logic work end-to-end without HPC?
    - 3.5 Document findings
        - This feeds directly into Milestone 2.

---

## Milestone 2
- **Description: Milestone 2...**

### Stages
#### Stage 4: Data Exploration + Preprocessing Setup
- **Goal: Provide plots,  explanations, and GitHub structure.**
    - 4.1 Add notebook showing full exploration
        - Include:
            - variable descriptions
            - histograms
            - maps
            - missing data checks
            - distributions and scales
    - 4.2 Document preprocessing plan
        - Regridding
        - Temporal matching
        - Feature engineering
        - Bloom threshold logic
    - 4.3 Commit to GitHub (Milestone2 branch)
        - Push notebooks
        - Push small parquet files
        - Update README with data exploration section
    - Submit link
#### Stage 5: SDSC HPC Pre‑Scaling Prep
- **Goal: Get ready for HPC before access is granted.**
    - 5.1 Modularize your preprocessing code
        - Split into clear functions:
            - load_raw_files
            - regrid_data
            - align_time
            - compute_features
            - export_parquet
    - 5.2 Abstract out local paths
        - Prepare path variables so switching to SDSC is trivial.
            - maybe setup small pipelie with config file? 
    - 5.3 Test scaling by using Dask’s local cluster
        - Simulate bigger workload
        - Verify memory usage
        - Estimate compute time

---

## Milestone 3:
— **Description: Milestone 3...**
#### Stage 6:  Full Preprocessing + First Model
- **Goal: Complete all preprocessing and build K-Means model.**
    - 6.1 Run full preprocessing (medium size)
        - Using your local Dask setup:
            - Combine SST + chlorophyll + ice
            - Produce final tidy parquet files
    - 6.2 Train K-Means model
        - Choose number of clusters using silhouette
        - Interpret clusters
        - Map cluster labels back onto the ocean
        - Document patterns (tropics, poles, etc.)
    - 6.3 Evaluate underfitting/overfitting
        - K-Means doesn’t “fit” traditionally, so you explain cluster separability and silhouette score
        - Include interpretation
    - 6.4 Write Milestone 3 section in README
        - Methods: exploration, preprocessing, K-Means
        - Results: maps, plots
        - Conclusion: next steps
    - Commit to Milestone3 branch.

#### Stage 7: SDSC Full Pipeline Execution (Once Access Granted)
- **Goal: Scale entire workflow to global, multi-year dataset.**
    - 7.1 Upload scripts to SDSC
        - Preprocessing scripts
        - Environment file
        - Small data sample for quick tests
    - 7.2 Launch Dask on SDSC cluster
        - Create Dask distributed client
        - Benchmark load, map, reduce operations
    - 7.3 Process entire dataset
        - Convert raw NetCDF/HDF5 to parquet at large scale
        - Store in project folder on SDSC storage
    - 7.4 Run Spark ML pipeline
        - Random Forest (bloom classifier)
        - XGBoost (chlorophyll regression)
        - Distributed correlation analysis
        - Collect outputs (model summaries, feature importances, global maps).

---
## Milestone 4
- **Description: Milestone 4...**
#### Stage 8: Second Model + Final Writeup
- **Goal: Produce final models and scientific-paper-style README.**
    - 8.1 Finalize Random Forest
        - Define bloom threshold (percentile-based)
        - Train/test split by region and time
        - Feature importance analysis
        - Evaluate accuracy and spatial error patterns
    - 8.2 Finalize XGBoost regression
        - Evaluate $R^{2}$ and RMSE
        - Create:
            - scatter plot observed vs predicted
            - global error map
            - residuals by latitude
    - 8.3 Perform spatial correlation analysis
        - Compute correlation SST vs chlorophyll
        - Make global map
        - Interpret latitudinal patterns
    - 8.4 Marine Heatwave case study
        - Select event
        - Compute SST anomaly vs chlorophyll anomaly
        - Compare model predictions vs observed
    - 8.5 Write final report (README)
        - Include:
            - Introduction
            - Full Methods
            - Results
            - Discussion
            - Conclusion
            - Collaboration section
    - 8.6 Make repo public

---

## Milestone 5
- **Description: Miestone 5...**
#### Stage 9: Voting + Presentation Prep
- **Goal: Prepare visually compelling outputs.**
    - 9.1 Prepare visuals
        - Cluster map
        - Prediction vs observation map
        - Marine heatwave before/after
        - Correlation map
    - 9.2 Submit your top 3 votes

#### Stage 10: Polishing (Optional)
- **Goal: Make this look like a research-grade project.**
    - 10.1 Add animations
        - SST anomaly movie
        - Chlorophyll time-lapse
        - Cluster evolution
    - 10.2 Add documentation
        - Architecture diagram
        - Data flow pipeline
        - Environment setup instructions
