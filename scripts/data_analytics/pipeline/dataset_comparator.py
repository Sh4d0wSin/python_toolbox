import argparse
import pandas as pd


def load_data(path):
    return pd.read_csv(path)


def compare_shape(df1, df2):
    # print row and column counts for both DataFrames
    # flag if they differ


    print("df1 rows:", df1.shape[0], "| df2 rows:", df2.shape[0])
    if df1.shape[0] != df2.shape[0]:
        print("WARNING: row counts differ!")

    print("df1 columns:", df1.shape[1], "| df2 columns:", df2.shape[1])
    if df1.shape[1] != df2.shape[1]:
        print("WARNING: column counts differ!")
    


    


def compare_columns(df1, df2):
    # check if both DataFrames have the same columns
    # print any columns that are missing or added
    set1 = set(df1.columns)
    set2 = set(df2.columns)

    missing_cols = set1 - set2  # columns in df1 but missing from df2
    added_cols = set2 - set1  # columns added in df2 that weren't in df

    if missing_cols:
        print("Missing from df2:", missing_cols)

    if added_cols:
        print("Added in df2:", added_cols)

    if not missing_cols and not added_cols:
        print("Columns match.")


def compare_values(df1, df2):
    try:
        diff = df1.compare(df2)
    except ValueError as e:
        print("Cannot compare:", e)
        return

    if diff.empty:
        print("No differences found.")
    else:
        print(diff)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("original")
    parser.add_argument("updated")
    args = parser.parse_args()

    df1 = load_data(args.original)
    df2 = load_data(args.updated)

    compare_shape(df1, df2)
    compare_columns(df1, df2)
    compare_values(df1, df2)


if __name__ == "__main__":
    main()
