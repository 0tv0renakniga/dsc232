import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path

# --- Config ---
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

FILES = {
    "SST (NOAA)": {
        "path": DATA_DIR / "oisst-avhrr-v02r01.20200101.nc",
        "var": "sst"
    },
    "Chlorophyll (VIIRS)": {
        "path": DATA_DIR / "JPSS1_VIIRS.20200101_20200108.L3m.8D.CHL.chlor_a.4km.nc",
        "var": "chlor_a"
    },
    "Sea Ice (NSIDC)": {
        "path": DATA_DIR / "sic_psn25_20200101_F17_v05r00.nc",
        "var": "cdr_seaice_conc"
    }
}

def analyze_dataset(name, info):
    print(f"Analyzing {name}...")
    ds = xr.open_dataset(info["path"])
    var_name = info["var"]
    data = ds[var_name]

    # 1. Get Physical Stats
    # Check encoding for what the 'nodata' value was on disk
    fill_val = data.encoding.get('_FillValue', 'Not Set')
    
    # Flatten to count valid/invalid pixels
    flat_data = data.values.flatten()
    total_pixels = flat_data.size
    nan_count = np.isnan(flat_data).sum()
    valid_pixels = total_pixels - nan_count
    
    # 2. Get Coordinate Bounds
    stats = {
        "Name": name,
        "Variable": var_name,
        "Dims": dict(ds.dims),
        "Fill Value (Disk)": fill_val,
        "Total Pixels": total_pixels,
        "NaN Pixels": nan_count,
        "Valid %": (valid_pixels / total_pixels) * 100,
        "Data Type": str(data.dtype),
        "Min Value": np.nanmin(flat_data),
        "Max Value": np.nanmax(flat_data),
    }

    # coordinate checks
    if 'lon' in ds.coords:
        stats['Lon Min'] = ds.lon.min().item()
        stats['Lon Max'] = ds.lon.max().item()
        stats['Res (Est)'] = abs(ds.lon[1] - ds.lon[0]).item() if len(ds.lon) > 1 else "N/A"
    else:
        stats['Lon Min'] = "N/A (Proj)"
        stats['Lon Max'] = "N/A (Proj)"
        stats['Res (Est)'] = "25km (Nominal)"

    return stats, flat_data

def main():
    report_lines = []
    report_lines.append("# Data Audit Report")
    report_lines.append("Generated automatically for Milestone 2 Data Exploration.\n")
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    stats_list = []

    for i, (name, info) in enumerate(FILES.items()):
        try:
            stats, flat_vals = analyze_dataset(name, info)
            stats_list.append(stats)
            
            # --- Text Report Generation ---
            report_lines.append(f"## {name}")
            report_lines.append(f"- **Variable:** `{stats['Variable']}`")
            report_lines.append(f"- **Dimensions:** {stats['Dims']}")
            report_lines.append(f"- **Coordinate Mismatch Check:**")
            report_lines.append(f"  - Longitude Range: {stats['Lon Min']} to {stats['Lon Max']}")
            report_lines.append(f"  - Resolution: {stats['Res (Est)']}")
            report_lines.append(f"- **Data Quality:**")
            report_lines.append(f"  - Original Fill Value: {stats['Fill Value (Disk)']}")
            report_lines.append(f"  - Missing Data (NaN): {stats['NaN Pixels']:,} ({100 - stats['Valid %']:.1f}%)")
            report_lines.append(f"  - Valid Range: {stats['Min Value']:.2f} to {stats['Max Value']:.2f}\n")

            # --- Plot Histogram ---
            # Remove NaNs for plotting
            valid_vals = flat_vals[~np.isnan(flat_vals)]
            
            # Log scale for Chlorophyll
            if "Chlorophyll" in name:
                axes[i].hist(valid_vals, bins=50, log=True, color='green', alpha=0.7)
                axes[i].set_title(f"{name} (Log Scale)")
                axes[i].set_xlabel("mg m^-3")
            else:
                axes[i].hist(valid_vals, bins=50, color='steelblue', alpha=0.7)
                axes[i].set_title(f"{name}")
            
            axes[i].set_ylabel("Pixel Count")
            axes[i].grid(True, alpha=0.3)

        except Exception as e:
            report_lines.append(f"## {name} - ERROR")
            report_lines.append(f"Failed to process: {e}\n")

    # Save Plot
    plt.tight_layout()
    plot_path = OUTPUT_DIR / "data_distributions.png"
    plt.savefig(plot_path)
    print(f"Saved distribution plot to {plot_path}")

    # Save Text Report
    report_path = OUTPUT_DIR / "data_audit_report.md"
    with open(report_path, "w") as f:
        f.write("\n".join(report_lines))
    print(f"Saved text report to {report_path}")

    # Print a quick summary of the mismatch to console
    print("\n--- CRITICAL MISMATCH SUMMARY ---")
    df_stats = pd.DataFrame(stats_list).set_index("Name")
    print(df_stats[["Lon Min", "Lon Max", "Res (Est)", "Valid %"]])

if __name__ == "__main__":
    main()
