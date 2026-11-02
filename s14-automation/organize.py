import shutil
from datetime import date
from pathlib import Path

KINDS = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Pictures": [".jpg", ".png"],
    "Spreadsheets": [".xlsx", ".csv"],
}

folder = Path("downloads")
for file in sorted(folder.iterdir()):
    if not file.is_file():
        continue
    for kind, suffixes in KINDS.items():
        if file.suffix in suffixes:
            target = folder / kind
            target.mkdir(exist_ok=True)
            shutil.move(file, target / file.name)
            print(f"{file.name} -> {kind}")

backup = shutil.make_archive(f"backup-{date.today()}", "zip", folder)
print("Backup:", Path(backup).name)
