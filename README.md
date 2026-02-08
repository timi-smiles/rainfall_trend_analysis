# Rainfall Trend Analysis (2005–2025)

A Python-based pipeline for analyzing long-term rainfall trends across **Benue**, **Kwara**, and **Niger** states in Nigeria. This project performs data cleaning, aggregation, statistical trend analysis using Mann-Kendall tests, and visualization.

## 📊 Features

- **Data Cleaning**: Processes raw daily rainfall data from Excel files
- **Temporal Aggregation**: Generates monthly and annual rainfall totals
- **Trend Analysis**: Mann-Kendall test with Sen's slope estimator for statistical significance
- **Visualization**: Produces time-series plots with trend lines for each state
- **Multiple Output Formats**: CSV and Excel files for easy reporting

## 📁 Project Structure

```
rainfall_trend_analysis/
├── data/                                    # Raw input Excel files (not included in repo)
├── outputs/
│   ├── tables/                              # Generated CSV/Excel outputs
│   │   ├── clean_daily_data.csv
│   │   ├── monthly_rainfall_totals.csv
│   │   ├── annual_rainfall_totals.csv
│   │   ├── trend_results_mk_sen.csv
│   │   └── rainfall_outputs.xlsx
│   ├── plots/                               # Generated visualizations
│   └── logs/                                # Analysis logs
├── src/
│   ├── 01_inspect_data.py                   # Data inspection and validation
│   ├── 02_clean_data.py                     # Data cleaning and preprocessing
│   ├── 03_aggregate_totals.py               # Monthly/annual aggregation
│   ├── 04_trend_tests.py                    # Mann-Kendall trend analysis
│   ├── 05_visualize.py                      # Generate plots
│   ├── 06_run_all.py                        # Run complete pipeline
│   └── config.py                            # Project configuration
├── requirements.txt                         # Python dependencies
└── README.md                                # This file
```

## 🛠️ Installation

### Prerequisites

- **Python 3.8+** (recommended: Python 3.11)
- pip (Python package manager)
- Git (optional, for cloning)

### Step 1: Clone or Download the Project

```bash
# Option A: Clone with Git
git clone <repository-url>
cd rainfall_trend_analysis

# Option B: Download and extract the ZIP file, then navigate to the folder
cd rainfall_trend_analysis
```

### Step 2: Create a Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**
- `pandas` - Data manipulation
- `numpy` - Numerical operations
- `openpyxl` - Excel file handling
- `matplotlib` - Visualization
- `scipy` - Statistical functions
- `pymannkendall` - Mann-Kendall trend tests

## 📥 Data Preparation

Place your raw Excel data files in the `data/` directory. The expected file is:

- `weather_data_3_states.xlsx` (with sheets: "Benue", "Kwara", "Niger")

Each sheet should contain:
- **Date** column: YYYYDDD format (e.g., 2005001 for January 1, 2005)
- **PCP** column: Daily precipitation in mm

> **Note:** If your filenames differ, update `src/config.py` to match your file names.

## 🚀 Usage

### Option 1: Run Complete Pipeline (Recommended)

Execute all analysis steps in sequence:

```bash
python -m src.06_run_all
```

This will:
1. Inspect raw data files
2. Clean and preprocess daily rainfall data
3. Aggregate into monthly and annual totals
4. Perform Mann-Kendall trend tests
5. Generate visualization plots

### Option 2: Run Individual Steps

Execute specific analysis modules:

```bash
# Inspect data
python -m src.01_inspect_data

# Clean data
python -m src.02_clean_data

# Aggregate totals
python -m src.03_aggregate_totals

# Run trend tests
python -m src.04_trend_tests

# Create visualizations
python -m src.05_visualize
```

## 📈 Output Files

### Tables (CSV Format)

Located in `outputs/tables/`:

| File | Description |
|------|-------------|
| `clean_daily_data.csv` | Cleaned daily rainfall records |
| `monthly_rainfall_totals.csv` | Monthly precipitation totals by state |
| `annual_rainfall_totals.csv` | Annual precipitation totals by state |
| `trend_results_mk_sen.csv` | Mann-Kendall test results with Sen's slope |
| `rainfall_outputs.xlsx` | Excel workbook with monthly and annual totals |

### Trend Results Interpretation

The `trend_results_mk_sen.csv` contains:

- **Trend**: Classification (increasing, decreasing, no trend)
- **H**: Hypothesis test result (1 = significant, 0 = not significant at α=0.05)
- **p_value**: Statistical significance level
- **z_value**: Mann-Kendall test statistic
- **tau**: Kendall's tau correlation coefficient
- **sen_slope_mm_per_year**: Rate of change (mm/year)
- **sen_intercept**: Y-intercept of trend line

### Plots

Located in `outputs/plots/`:

- `benue_annual_rainfall.png`
- `kwara_annual_rainfall.png`
- `niger_annual_rainfall.png`

Each plot shows:
- Annual rainfall totals (2005-2025)
- 3-year moving average trend line

## 🔧 Configuration

Edit `src/config.py` to customize:

- Input file paths
- Output directory locations
- Data file names

Example:
```python
FILE_3_STATES = DATA_DIR / "your_custom_filename.xlsx"
```

## 📊 Sample Results

**Example Mann-Kendall Test Output:**

```
State  | Trend      | p_value | Sen Slope (mm/yr) | Significant
-------|------------|---------|-------------------|-------------
Benue  | no trend   | 0.928   | -1.99             | No
Kwara  | increasing | 0.050   | 16.68             | Yes
Niger  | increasing | 0.050   | 28.20             | Yes
```

## 🐛 Troubleshooting

### Common Issues

**1. Import Error: No module named 'src'**
- Solution: Run commands with `python -m src.module_name` format
- Ensure you're in the project root directory

**2. File Not Found Error**
- Check that data files are in the `data/` folder
- Verify file names in `src/config.py` match your actual files

**3. Excel Read Error**
- Ensure `openpyxl` is installed: `pip install openpyxl`
- Check that Excel files are not corrupted or password-protected

**4. Python Version Issues**
- Minimum requirement: Python 3.8
- Recommended: Python 3.11

## 📝 Requirements

See `requirements.txt` for complete list:

```
pandas
numpy
openpyxl
matplotlib
scipy
pymannkendall
```

## 🤝 Contributing

Feel free to:
- Report bugs or issues
- Suggest new features
- Submit pull requests

## 📄 License

This project is available for academic and research purposes.

## 📧 Contact

For questions or support, please contact the project maintainer.

---

**Last Updated:** February 2026  
**Python Version:** 3.8+  
**Analysis Period:** 2005–2025
