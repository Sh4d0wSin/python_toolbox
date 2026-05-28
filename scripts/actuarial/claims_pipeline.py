import pandas as pd
import glob 
import argparse



def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("target")

    recorded = parser.parse_args()


    all_csvs = glob.glob(recorded.target + "/*.csv")

    concat = pd.concat([pd.read_csv(csv) for csv in all_csvs]).drop_duplicates()

    concat.to_csv("cleaned_claims.csv")

    amount_claims = len(concat)

    avg_claim_amount = concat["claim_amount"].mean()

    print("amount of claims:", amount_claims)
    print("average claim amount:", avg_claim_amount)
    

    concat.groupby("line_of_business")["claim_amount"].agg(["sum", "count"]).to_csv("summary_report.csv")


     




   

     



if __name__ == "__main__":
    main()
   