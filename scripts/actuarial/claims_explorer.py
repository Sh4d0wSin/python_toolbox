import pandas as pd



def main():

    read_csv = pd.read_csv("claims.csv")

    print(read_csv.head())
    print(read_csv.info())
    print(read_csv.describe())


    open_claims = read_csv[read_csv["status"] == "open"]

    group_by_lias = open_claims.groupby("line_of_business")["claim_amount"].sum()

    sort_by_sums = group_by_lias.sort_values(ascending=False)

    print("new cvs:", sort_by_sums)
    sort_by_sums.to_csv("open_claims_summary.csv")


     









if __name__ == "__main__":
    main()
   