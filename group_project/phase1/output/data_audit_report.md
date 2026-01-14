# Data Audit Report
Generated automatically for Milestone 2 Data Exploration.

## SST (NOAA)
- **Variable:** `sst`
- **Dimensions:** {'time': 1, 'zlev': 1, 'lat': 720, 'lon': 1440}
- **Coordinate Mismatch Check:**
  - Longitude Range: 0.125 to 359.875
  - Resolution: 0.25
- **Data Quality:**
  - Original Fill Value: -999
  - Missing Data (NaN): 345,650 (33.3%)
  - Valid Range: -1.80 to 32.23

## Chlorophyll (VIIRS)
- **Variable:** `chlor_a`
- **Dimensions:** {'lat': 4320, 'lon': 8640, 'rgb': 3, 'eightbitcolor': 256}
- **Coordinate Mismatch Check:**
  - Longitude Range: -179.9791717529297 to 179.9791717529297
  - Resolution: 0.0416717529296875
- **Data Quality:**
  - Original Fill Value: -32767.0
  - Missing Data (NaN): 22,530,043 (60.4%)
  - Valid Range: 0.00 to 67.97

## Sea Ice (NSIDC)
- **Variable:** `cdr_seaice_conc`
- **Dimensions:** {'time': 1, 'y': 448, 'x': 304}
- **Coordinate Mismatch Check:**
  - Longitude Range: N/A (Proj) to N/A (Proj)
  - Resolution: 25km (Nominal)
- **Data Quality:**
  - Original Fill Value: 255
  - Missing Data (NaN): 68,789 (50.5%)
  - Valid Range: 0.00 to 1.00
