import pandas as pd




def main():

    claim_rep = pd.DataFrame([{"policy_id": 1, "claim_amount": 1500.00}, {"policy_id": 2, "claim_amount": 2300.00}])
    policy_rep = pd.DataFrame([{"policy_id": 1, "premium": 20000}, {"policy_id": 2, "premium": 15000}, {"policy_id": 3, "premium": 500}])

    merged_view = pd.merge(claim_rep, policy_rep, on="policy_id", how="outer")


    merged_view = merged_view.fillna(0)

    merged_view["claim_ratio"] = merged_view["claim_amount"] / merged_view["premium"]


    merged_view.to_excel("merged_claim_policy.xlsx", sheet_name = "Merged_Claim_Policy")


if __name__ == "__main__":
    main()
   