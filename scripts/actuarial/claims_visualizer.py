import pandas as pd
import matplotlib.pyplot as plt



def main():

    read_csv = pd.read_csv("claims.csv")

    
    better_view =  read_csv.groupby("line_of_business")["claim_amount"].sum()
    plt.bar(better_view.index, better_view.values)

    plt.title("Total Claim Amount by Line of Business")
    plt.xlabel("Line of Business")
    plt.ylabel("Total Claim Amount")


    plt.savefig("bar_chart.png")


    plt.clf()

    
    read_csv["date"] = pd.to_datetime(read_csv["date"])


    read_csv["month"] = read_csv["date"].dt.month

    line_chart =  read_csv.groupby("month")["claim_amount"].sum()


    plt.plot(line_chart.index, line_chart.values)

    plt.title("Claim Amount Trend by Month")
    plt.xlabel("Month")
    plt.ylabel("Total Claim Amount")

    plt.savefig("line_chart.png")






if __name__ == "__main__":
    main()
   