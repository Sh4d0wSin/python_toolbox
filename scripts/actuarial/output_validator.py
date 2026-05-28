import numpy as np
import pandas as pd






def main():

    python_rep = pd.DataFrame([{"claim_id": 1, "claim_amount": 1500.00}, {"claim_id": 2, "claim_amount": 2300.00}])


    sas_rep = pd.DataFrame([{"claim_id": 1, "claim_amount": 1500.01}, {"claim_id": 2, "claim_amount": 2300.00}])


     
   



    if python_rep.equals(sas_rep):
        print("equal")
    else:
        print("not equal:", python_rep.compare(sas_rep))


    check_true_errors = np.isclose(python_rep["claim_amount"], sas_rep["claim_amount"])


    print("Numpy verdict:", check_true_errors)



if __name__ == "__main__":
    main()