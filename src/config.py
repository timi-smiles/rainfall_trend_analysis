from pathlib import Path

# Project root is the folder that contains "src/"
PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
TABLES_DIR = OUTPUT_DIR / "tables"
PLOTS_DIR = OUTPUT_DIR / "plots"
LOGS_DIR = OUTPUT_DIR / "logs"

# Input files (edit names here if your filenames differ)
FILE_3_STATES = DATA_DIR / "weather_data_3_states.xlsx"
FILE_ILORIN = DATA_DIR / "Ilorin 2022 -2024 (Autosaved) (1).xlsx"
FILE_NIMET_ORIGINAL = DATA_DIR / "original NIMET Climate Data (1).xlsx"

def ensure_output_dirs() -> None:
    """Create output folders if they don't exist."""
    for d in [OUTPUT_DIR, TABLES_DIR, PLOTS_DIR, LOGS_DIR]:
        d.mkdir(parents=True, exist_ok=True)
