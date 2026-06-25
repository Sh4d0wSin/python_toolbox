import argparse
import pandas as pd


def load_data(path):
    # load the CSV into a DataFrame
    read_csv = pd.read_csv(path)
    
    return read_csv


def profile_overview(df):
    # print total row count and column count
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])



def profile_columns(df):
    # for each column, print:
    # - column name and data type
    # - null count
    # - unique value count
    for col in df.columns:
        print(col, df[col].dtype)
        print("Nulls:", df[col].isnull().sum())
        print("Unique values:", df[col].nunique())



def profile_numeric(df):
    # filter to numeric columns only
    # for each numeric column, print min, max, and mean
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            print(col)
            print("Min:", df[col].min())
            print("Max:", df[col].max())
            print("Mean:", df[col].mean())

    


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()

    df = load_data(args.path)

    profile_overview(df)
    profile_columns(df)
    profile_numeric(df)


if __name__ == "__main__":
    main()
