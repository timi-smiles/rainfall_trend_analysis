import pandas as pd
from datetime import datetime, timedelta
from src.config import FILE_3_STATES, TABLES_DIR, ensure_output_dirs


def parse_yyyyddd(value: int) -> datetime:
    """
    Convert YYYYDDD format (e.g., 2005001) into a real datetime.
    """
    value = int(value)
    year = value // 1000
    day_of_year = value % 1000
    return datetime(year, 1, 1) + timedelta(days=day_of_year - 1)


def clean_state_sheet(sheet_name: str) -> pd.DataFrame:
    print(f"Cleaning sheet: {sheet_name}")

    df = pd.read_excel(FILE_3_STATES, sheet_name=sheet_name)

    # Keep only what we need
    df = df[["Date", "PCP"]].copy()

    # Convert date
    df["Date"] = df["Date"].apply(parse_yyyyddd)

    # Ensure rainfall is numeric
    df["PCP"] = pd.to_numeric(df["PCP"], errors="coerce")

    # Add state column
    df["State"] = sheet_name

    return df


def main():
    ensure_output_dirs()

    sheets = ["Kwara", "Benue", "Niger"]

    all_data = []
    for sheet in sheets:
        cleaned = clean_state_sheet(sheet)
        all_data.append(cleaned)

    master_df = pd.concat(all_data, ignore_index=True)

    # Sort properly for time series analysis
    master_df = master_df.sort_values(by=["State", "Date"])

    output_path = TABLES_DIR / "clean_daily_data.csv"
    master_df.to_csv(output_path, index=False)

    print(f"\n✅ Cleaned daily data saved to: {output_path}")
    print(master_df.head())


if __name__ == "__main__":
    main()
