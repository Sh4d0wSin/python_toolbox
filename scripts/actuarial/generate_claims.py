import pandas as pd
import random
import argparse
import datetime




def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--rows", default=25, type=int )


    number = parser.parse_args()

    line_of_business = ["Motor", "Liability", "Property"]
    status = ["open", "closed"]


    starter_date = datetime.date(2025, 1, 1)
    

    table = []
    for _ in range(0,number.rows):

        table.append({"date": starter_date + datetime.timedelta(days=random.randint(0, 365))  ,"line_of_business": random.choice(line_of_business), "claim_amount":round(random.uniform(500, 50000),2), "status": random.choice(status)})


    data_frame =  pd.DataFrame(table)

    gen_csv = data_frame.to_csv("claims.csv", index=False)



     









if __name__ == "__main__":
    main()
   