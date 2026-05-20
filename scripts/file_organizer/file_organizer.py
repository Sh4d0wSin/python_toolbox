import argparse 
import pathlib
import shutil 




    

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("target")


    recorded_folder = parser.parse_args()

    path = pathlib.Path(recorded_folder.target)

    categories = {".pdf": "Documents",
                ".txt": "Documents",
                ".mp3": "Music",
                ".mp4": "Videos",
                ".py": "Scripts",
                ".java": "Projects"}

    for file in path.iterdir():
        if file.is_file():
            if categories.get(file.suffix) is not None:
                print(file.name, "belongs to", categories.get(file.suffix))

                ordered = path / categories.get(file.suffix)
                ordered.mkdir(exist_ok=True)
                shutil.move(file, ordered)








if __name__ == "__main__":
    main()
   