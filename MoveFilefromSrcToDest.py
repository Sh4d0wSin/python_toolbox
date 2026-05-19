import shutil 
import pathlib

path = pathlib.Path(r"C:\Users\GBT A520M RADEON\Desktop\Own projects\python_toolbox")

source = path / "SourceFolder" / "dummy1.txt"


dest = path / "DestFolder"


shutil.move(source, dest)