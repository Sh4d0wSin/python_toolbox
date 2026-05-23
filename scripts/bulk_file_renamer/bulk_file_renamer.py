import pathlib
import argparse
import re




def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("target")
    parser.add_argument("--prefix", default="")
    parser.add_argument("--suffix", default="")
    parser.add_argument("--replace")
    parser.add_argument("--replacement")
    parser.add_argument("--dry-run",action="store_true")


    recorded = parser.parse_args()

    directory = pathlib.Path(recorded.target)



    for file in directory.iterdir():
        if file.is_file():
            base = file.stem
            
            

            if recorded.replace and recorded.replacement:
               base = re.sub(recorded.replace, recorded.replacement,  base)
               

            new_name = recorded.prefix + base + recorded.suffix + file.suffix


            if not recorded.dry_run:
                file.rename(file.parent / new_name)
            else:
                print(file.name, "->", new_name)





     









if __name__ == "__main__":
    main()
   