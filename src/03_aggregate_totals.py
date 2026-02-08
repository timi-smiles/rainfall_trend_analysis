import pandas as pd
from src.config import TABLES_DIR, ensure_output_dirs


def main():
    ensure_output_dirs()

    input_path = TABLES_DIR / "clean_daily_data.csv"
    if not input_path.exists():
        raise FileNotFoundError(
            f"Missing {input_path}. Run: python -m src.02_clean_data first."
        )

    df = pd.read_csv(input_path)

    # Convert Date back to datetime
    df["Date"] = pd.to_datetime(df["Date"])

    # Create Year and Month columns
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month

    # Monthly totals (sum of daily PCP)
    monthly = (
        df.groupby(["State", "Year", "Month"], as_index=False)["PCP"]
        .sum()
        .rename(columns={"PCP": "Monthly_Rainfall_mm"})
        .sort_values(["State", "Year", "Month"])
    )

    # Annual totals (sum of daily PCP)
    annual = (
        df.groupby(["State", "Year"], as_index=False)["PCP"]
        .sum()
        .rename(columns={"PCP": "Annual_Rainfall_mm"})
        .sort_values(["State", "Year"])
    )

    # Save CSV outputs
    monthly_path = TABLES_DIR / "monthly_rainfall_totals.csv"
    annual_path = TABLES_DIR / "annual_rainfall_totals.csv"

    monthly.to_csv(monthly_path, index=False)
    annual.to_csv(annual_path, index=False)

    print(f"✅ Monthly totals saved to: {monthly_path}")
    print(f"✅ Annual totals saved to: {annual_path}")

    # ✅ Also export as Excel for easy reporting
    excel_path = TABLES_DIR / "rainfall_outputs.xlsx"
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        monthly.to_excel(writer, sheet_name="Monthly_Totals", index=False)
        annual.to_excel(writer, sheet_name="Annual_Totals", index=False)

    print(f"✅ Excel export saved to: {excel_path}")

    print("\nPreview (Annual Totals):")
    print(annual.head(10))


if __name__ == "__main__":
    main()
