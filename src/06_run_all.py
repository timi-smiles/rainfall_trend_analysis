import subprocess
import sys


def run(module_name: str) -> None:
    print("\n" + "=" * 80)
    print(f"Running: {module_name}")
    print("=" * 80)

    result = subprocess.run([sys.executable, "-m", module_name], text=True)
    if result.returncode != 0:
        raise SystemExit(f" Failed at step: {module_name}")


def main():
    run("src.01_inspect_data")
    run("src.02_clean_data")
    run("src.03_aggregate_totals")
    run("src.04_trend_tests")
    run("src.05_visualize")

    print("\n✅ ALL STEPS COMPLETED SUCCESSFULLY.")
    print("Check outputs/tables and outputs/plots for your results.")


if __name__ == "__main__":
    main()
