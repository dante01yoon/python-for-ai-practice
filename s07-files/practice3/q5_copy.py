import os
import shutil
from pathlib import Path

Path("backup").mkdir(exist_ok=True)
for path in Path("notes").glob("*.txt"):
    shutil.copy(path, Path("backup", path.name))

Path("archive").mkdir(exist_ok=True)
shutil.move("notes/monday.txt", "archive/monday.txt")
print(sorted(os.listdir("backup")))
print(sorted(os.listdir("notes")))
