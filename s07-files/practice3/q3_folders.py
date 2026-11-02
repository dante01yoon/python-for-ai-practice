from pathlib import Path

for month in ["2026-10", "2026-11", "2026-12"]:
    Path("reports", month).mkdir(parents=True, exist_ok=True)

for folder in sorted(Path("reports").iterdir()):
    print(folder, folder.is_dir())
