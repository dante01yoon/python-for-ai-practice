from pathlib import Path

phone = {p.name for p in Path("phone").iterdir()}
backup = {p.name for p in Path("backup").iterdir()}
print("Not backed up yet:", sorted(phone - backup))
print("Only in the backup:", sorted(backup - phone))
