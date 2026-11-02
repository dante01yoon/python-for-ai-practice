from pathlib import Path

files = [p for p in Path(".venv").rglob("*") if p.is_file()]
files.sort(key=lambda p: p.stat().st_size, reverse=True)
for p in files[:5]:
    print(f"{p.stat().st_size / 1024:8.0f} KB  {p.name}")
print(len(files), "files in total")
