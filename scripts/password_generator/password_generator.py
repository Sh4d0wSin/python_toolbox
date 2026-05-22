import argparse
import secrets
import string



def main():
    parser = argparse.ArgumentParser()


    parser.add_argument("--len", default=12, type=int)
    parser.add_argument("--digits", action="store_true")
    parser.add_argument("--uppercase", action="store_true")
    parser.add_argument("--symbols", action="store_true")


    args= parser.parse_args()

    pool = string.ascii_lowercase

    if args.digits:
       pool += string.digits 

    if args.uppercase:
       pool += string.ascii_uppercase
    
    if args.symbols:
       pool += string.punctuation

    password= ""
    for _ in range(args.len):
       password += secrets.choice(pool)

    print("Your password:",  password)



if __name__ == "__main__":
    main()
   