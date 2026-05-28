# Actuarial Data Scripts

A collection of Python scripts simulating actuarial data workflows — covering data generation, exploration, aggregation, pipeline processing, and output validation. Built using `pandas`, `numpy`, and the Python standard library.

## Setup

```bash
pip install pandas numpy
```

---

## Scripts

### `generate_claims.py`
Generates a synthetic claims dataset and saves it to `claims.csv`. Accepts a `--rows` argument to control the number of rows generated (default: 25). Each row contains a random date, line of business (Motor / Liability / Property), claim amount, and status (open / closed).

```bash
python generate_claims.py --rows 50
```

---

### `claims_explorer.py`
Reads `claims.csv` and produces a filtered summary. Prints basic DataFrame info (`head`, `info`, `describe`), filters to open claims only, groups by line of business, sums claim amounts, sorts largest first, and saves the result to `open_claims_summary.csv`.

```bash
python claims_explorer.py
```

---

### `monthly_aggregator.py`
Reads `claims.csv`, converts the date column to datetime, extracts the month, and groups by month and line of business. Calculates mean claim amount and claim count per group. Saves the result to `monthly_claims_summary.csv`.

```bash
python monthly_aggregator.py
```

---

### `claims_pipeline.py`
Reads all CSV files from a given directory, concatenates them into a single DataFrame, removes duplicate rows, and generates a summary report (total claims, average amount, and totals per line of business). Saves cleaned data to `cleaned_claims.csv` and the summary to `summary_report.csv`.

```bash
python claims_pipeline.py "path/to/directory"
```

---

### `output_validator.py`
Simulates a SAS vs Python output comparison. Creates two DataFrames with slight value differences, checks equality with `.equals()`, shows discrepancies with `.compare()`, and applies a floating point tolerance check using `numpy.isclose()` to distinguish real differences from floating point noise.

```bash
python output_validator.py
```

---

### `claims_visualizer.py` *(in progress)*
Will produce bar and line charts from claims data using `matplotlib`.

---

### `policy_merger.py` *(in progress)*
Will simulate a Power Query-style merge of two data sources on a shared key, fill missing values, compute a derived column, and export to Excel.
