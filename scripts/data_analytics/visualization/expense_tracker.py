import argparse
import pandas as pd
import matplotlib.pyplot as plt


def load_data(path):
    # load the CSV into a DataFrame
    # parse the date column as datetime
    read_csv = pd.read_csv(path)
    read_csv["date"] = pd.to_datetime(read_csv["date"])
    return read_csv


def summarize_by_category(df):
    # group by category column and sum the amount column


    return df.groupby("category")["amount"].sum()



def summarize_by_month(df):
    # extract month from date column
    # group by month and sum the amount column
    df["month"] = df["date"].dt.to_period("M")
    return df.groupby("month")["amount"].sum()

    


def plot_pie(category_totals):
    # create a pie chart of spending by category
    # add a title
    # save or show the chart

    plt.pie(category_totals.values, labels=category_totals.index, autopct="%1.1f%%")
    plt.title("Spending by Category")
    plt.show()


def plot_bar(monthly_totals):
    # create a bar chart of total spending per month
    # label the x and y axes
    # add a title
    # save or show the chart
    plt.bar(monthly_totals.index.astype(str), monthly_totals.values)
    plt.xlabel("Month")
    plt.ylabel("Total Spending")
    plt.title("Monthly Spending")
    plt.show()


def main():
    # set up argparse and add an argument for the CSV path
    parser = argparse.ArgumentParser()

    parser.add_argument("path")

    target = parser.parse_args()


    # call load_data() with the path
    df = load_data(target.path)

    # call summarize_by_category() and print the result
    category_totals = summarize_by_category(df)
    print(category_totals)

    # call summarize_by_month() and print the result
    monthly_totals = summarize_by_month(df)
    print(monthly_totals)

    # call plot_pie() with the category totals
    plot_pie(category_totals)

    # call plot_bar() with the monthly totals
    plot_bar(monthly_totals)


if __name__ == "__main__":
    main()
