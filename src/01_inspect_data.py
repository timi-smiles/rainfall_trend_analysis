import pandas as pd
from src.config import (
    FILE_3_STATES,
    FILE_ILORIN,
    FILE_NIMET_ORIGINAL,
    ensure_output_dirs,
)

pd.set_option("display.max_columns", 50)
pd.set_option("display.width", 140)


def inspect_excel(path, max_rows: int = 8) -> None:
    print("\n" + "=" * 90)
    print(f"FILE: {path}")
    print("=" * 90)

    if not path.exists():
        print("❌ File not found. Check the filename in data/ or config.py")
        return

    try:
        xl = pd.ExcelFile(path)
        print(f"Sheets found: {xl.sheet_names}")

        for sheet in xl.sheet_names:
            print("\n" + "-" * 90)
            print(f"SHEET: {sheet}")
            print("-" * 90)

            df = xl.parse(sheet_name=sheet)
            print(f"Shape: {df.shape}")
            print("Columns:", list(df.columns))

            print("\nHead:")
            print(df.head(max_rows))

            print("\nMissing values (top 10 columns):")
            na_counts = df.isna().sum().sort_values(ascending=False)
            print(na_counts.head(10))

    except Exception as e:
        print(f"❌ Failed to read: {e}")


def main():
    ensure_output_dirs()

    # Inspect all available datasets (we'll choose the cleanest for the core analysis)
    inspect_excel(FILE_3_STATES)
    inspect_excel(FILE_ILORIN)
    inspect_excel(FILE_NIMET_ORIGINAL)

    print("\n✅ Inspection complete.")
    print("Next step: we decide which file(s) have clean Date + rainfall columns to clean and aggregate.")


if __name__ == "__main__":
    main()
