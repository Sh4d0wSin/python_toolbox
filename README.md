# python_toolbox

Practical Python CLI tools and data scripts covering file management, security, data processing, and visualization.

---

## Scripts

### `password_generator/`
- CLI tool that generates a secure random password using `secrets`
- Supports `--len`, `--digits`, `--uppercase`, and `--symbols` flags

### `file_organizer/`
- Organizes files in a directory by moving them into subfolders by file extension
- Accepts a target directory as a CLI argument

### `bulk_file_renamer/`
- Renames files in bulk with support for prefix, suffix, and regex find/replace
- Includes a `--dry-run` flag to preview changes before applying them

### `System_info_script/`
- Displays system information including OS, hostname, CPU count, RAM, and disk usage
- Uses `platform` (standard library) and `psutil`

### `log_analyzer/`
- Parses a log file and counts occurrences of `ERROR`, `WARNING`, and `INFO` level entries
- Accepts a log file path as a CLI argument and prints a summary report
- Includes a `sample.log` file for quick testing

### `data_analytics/`
A suite of data analytics scripts organised by category:

**`visualization/`**
- **`expense_tracker.py`** — reads a transactions CSV, summarizes spending by category and month, and renders a pie chart and bar chart using `matplotlib`

**`pandas_numpy/`**
- **`csv_profiler.py`** — profiles any CSV and reports row/column counts, data types, null counts, unique value counts, and min/max/mean for numeric columns

**`pipeline/`**
- **`dataset_comparator.py`** — compares two CSVs and reports shape differences, added/missing columns, and changed values using `pandas.DataFrame.compare()`

---

### `actuarial/`
A suite of scripts simulating actuarial data workflows:
- **`generate_claims.py`** — generates a synthetic claims CSV with random dates, lines of business, amounts, and statuses
- **`claims_explorer.py`** — filters, groups, and summarizes open claims by line of business
- **`monthly_aggregator.py`** — aggregates mean claim amount and count by month and line of business
- **`claims_pipeline.py`** — merges multiple CSVs, removes duplicates, and produces a summary report
- **`output_validator.py`** — compares two DataFrames for discrepancies using `.equals()`, `.compare()`, and `numpy.isclose()`
- **`claims_visualizer.py`** — produces bar and line charts from claims data using `matplotlib`
- **`policy_merger.py`** — merges claims and policy data on a shared key, fills missing values, computes claim ratio, and exports to Excel
