import pandas as pd



def main():
    read_csv = pd.read_csv("claims.csv")

    read_csv["date"] = pd.to_datetime(read_csv["date"])


    read_csv["month"] = read_csv["date"].dt.month



   

    group_by_month = read_csv.groupby(["month", "line_of_business"])["claim_amount"].agg(["mean", "count"])

   
    
    print(group_by_month)
    group_by_month.to_csv("monthly_claims_summary.csv")








if __name__ == "__main__":
    main()
   