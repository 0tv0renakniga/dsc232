import os
import requests
from pathlib import Path
from tqdm import tqdm
from getpass import getpass
import netrc
import datetime

# --- Configuration ---
TARGET_YEAR = 2020
TARGET_MONTH = 1  # January
DAYS_IN_MONTH = 31

# Paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "phase2" / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# NASA Earthdata Login (Required for Chlorophyll)
URS_URL = 'https://urs.earthdata.nasa.gov'

def get_nasa_session():
    """Creates a requests Session with Earthdata authentication."""
    session = requests.Session()
    try:
        info = netrc.netrc()
        login, _, password = info.authenticators('urs.earthdata.nasa.gov')
        session.auth = (login, password)
        print("   [Auth] Using credentials from ~/.netrc")
    except (FileNotFoundError, TypeError):
        print("\n--- NASA Earthdata Login Required ---")
        user = input("Username: ")
        password = getpass("Password: ")
        session.auth = (user, password)
    return session

def download_file(url, filename, session=None):
    dest_path = DATA_DIR / filename
    if dest_path.exists():
        print(f"   [Skip] {filename} exists.")
        return

    print(f"   [Down] Downloading {filename}...")
    try:
        caller = session if session else requests
        with caller.get(url, stream=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            with open(dest_path, 'wb') as f, tqdm(
                total=total_size, unit='iB', unit_scale=True, desc=filename, leave=False
            ) as bar:
                for chunk in r.iter_content(chunk_size=8192):
                    size = f.write(chunk)
                    bar.update(size)
    except Exception as e:
        print(f"   [Error] Failed to download {filename}: {e}")
        if dest_path.exists(): dest_path.unlink()

def main():
    print(f"--- Bulk Data Downloader: {TARGET_YEAR}-{TARGET_MONTH:02d} ---")
    
    # 1. NOAA OISST (Daily)
    print("\n1. Fetching NOAA OISST (SST)...")
    base_sst = f"https://www.ncei.noaa.gov/data/sea-surface-temperature-optimum-interpolation/v2.1/access/avhrr/{TARGET_YEAR}{TARGET_MONTH:02d}/"
    for day in range(1, DAYS_IN_MONTH + 1):
        fname = f"oisst-avhrr-v02r01.{TARGET_YEAR}{TARGET_MONTH:02d}{day:02d}.nc"
        download_file(base_sst + fname, fname)

    # 2. NSIDC Sea Ice (Daily)
    print("\n2. Fetching NSIDC Sea Ice...")
    base_ice = f"https://noaadata.apps.nsidc.org/NOAA/G02202_V5/north/daily/{TARGET_YEAR}/"
    for day in range(1, DAYS_IN_MONTH + 1):
        fname = f"sic_psn25_{TARGET_YEAR}{TARGET_MONTH:02d}{day:02d}_F17_v05r00.nc"
        download_file(base_ice + fname, fname)

    # 3. NASA VIIRS Chlorophyll (DAILY)
    print("\n3. Fetching NASA VIIRS Chlorophyll (Daily)...")
    session = get_nasa_session()
    
    # URL Pattern: https://oceandata.sci.gsfc.nasa.gov/ob/getfile/JPSS1_VIIRS.YYYYMMDD.L3m.DAY.CHL.chlor_a.4km.nc
    for day in range(1, DAYS_IN_MONTH + 1):
        dt = datetime.date(TARGET_YEAR, TARGET_MONTH, day)
        d_str = dt.strftime("%Y%m%d")
        
        # New Daily Filename Format
        fname = f"JPSS1_VIIRS.{d_str}.L3m.DAY.CHL.chlor_a.4km.nc"
        url = f"https://oceandata.sci.gsfc.nasa.gov/ob/getfile/{fname}"
        
        download_file(url, fname, session)

    print("\n--- Download Complete ---")

if __name__ == "__main__":
    main()
