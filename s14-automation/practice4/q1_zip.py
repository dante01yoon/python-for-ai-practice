import shutil
from datetime import date
from pathlib import Path

archive = Path(shutil.make_archive(f"notes-backup-{date.today()}", "zip", "notes"))
print("Created", archive.name)
print(f"{archive.stat().st_size} bytes")
