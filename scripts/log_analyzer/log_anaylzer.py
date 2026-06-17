import argparse, re, pathlib



def main():

    parser = argparse.ArgumentParser()


    parser.add_argument("log")

    recorded = parser.parse_args()


    log_path = pathlib.Path(recorded.log)

    ERROR = WARNING = INFO = 0


    with open(log_path) as f:

        for line in f:

            if re.search("ERROR", line):
                ERROR += 1
            elif re.search("WARNING", line):
                WARNING += 1
            elif re.search("INFO", line):
                INFO += 1


    print("------------------SUMMARY REPORT----------------")
    print("AMOUNT ERROR LOGS:", ERROR)
    print("AMOUNT WARNING LOGS:", WARNING)
    print("AMOUNT INFO LOGS:", INFO)
    






if __name__ == "__main__":
    main()
    
   