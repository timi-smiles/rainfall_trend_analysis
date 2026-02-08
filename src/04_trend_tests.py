import pandas as pd
import pymannkendall as mk
from src.config import TABLES_DIR, ensure_output_dirs


def run_mk_for_state(state_df: pd.DataFrame) -> dict:
    """
    Runs Mann-Kendall + Sen slope on a state's annual rainfall time series.

    Expects columns:
      - Year
      - Annual_Rainfall_mm
    """
    state_df = state_df.sort_values("Year")
    years = state_df["Year"].to_list()
    series = state_df["Annual_Rainfall_mm"].to_list()

    # pymannkendall needs a 1D sequence of numbers in time order
    result = mk.original_test(series)

    return {
        "State": state_df["State"].iloc[0],
        "Start_Year": years[0],
        "End_Year": years[-1],
        "N_Years": len(years),
        "Trend": result.trend,           # 'increasing', 'decreasing', or 'no trend'
        "H": int(result.h),              # 1 = significant trend, 0 = not significant (at alpha=0.05)
        "p_value": float(result.p),
        "z_value": float(result.z),
        "tau": float(result.Tau),
        "s_statistic": float(result.s),
        "sen_slope_mm_per_year": float(result.slope),
        "sen_intercept": float(result.intercept),
    }


def main():
    ensure_output_dirs()

    annual_path = TABLES_DIR / "annual_rainfall_totals.csv"
    if not annual_path.exists():
        raise FileNotFoundError(
            f"Missing {annual_path}. Run: python -m src.03_aggregate_totals first."
        )

    annual = pd.read_csv(annual_path)

    results = []
    for state, state_df in annual.groupby("State"):
        stats = run_mk_for_state(state_df)
        results.append(stats)

    results_df = pd.DataFrame(results).sort_values("State")

    out_path = TABLES_DIR / "trend_results_mk_sen.csv"
    results_df.to_csv(out_path, index=False)

    print(f"✅ Trend results saved to: {out_path}\n")
    print(results_df)


if __name__ == "__main__":
    main()
