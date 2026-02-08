import pandas as pd
import matplotlib.pyplot as plt
from src.config import TABLES_DIR, PLOTS_DIR, ensure_output_dirs


def plot_state(state_df: pd.DataFrame):
    state = state_df["State"].iloc[0]
    state_df = state_df.sort_values("Year")

    x = state_df["Year"]
    y = state_df["Annual_Rainfall_mm"]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker="o")
    
    # Simple linear fit just for visual trend direction
    z = pd.Series(y).rolling(window=3, min_periods=1).mean()
    plt.plot(x, z, linestyle="--")

    plt.title(f"Annual Rainfall Trend for {state} (2005–2025)")
    plt.xlabel("Year")
    plt.ylabel("Annual Rainfall (mm)")
    plt.grid(True)

    out_file = PLOTS_DIR / f"{state.lower()}_annual_rainfall.png"
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()

    print(f"✅ Plot saved: {out_file}")


def main():
    ensure_output_dirs()

    annual_path = TABLES_DIR / "annual_rainfall_totals.csv"
    annual = pd.read_csv(annual_path)

    for state, state_df in annual.groupby("State"):
        plot_state(state_df)


if __name__ == "__main__":
    main()
