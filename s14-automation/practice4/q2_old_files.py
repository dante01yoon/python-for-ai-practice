import time
from pathlib import Path

DAY = 24 * 60 * 60
now = time.time()
for p in sorted(Path("downloads").iterdir()):
    age = (now - p.stat().st_mtime) / DAY
    if age > 30:
        print(f"would delete {p.name:<22} {age:4.0f} days old")
