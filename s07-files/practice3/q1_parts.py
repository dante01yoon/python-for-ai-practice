from pathlib import Path

for path in sorted(Path("notes").glob("*.txt")):
    print(path.name, path.stem, path.suffix, path.stat().st_size, "bytes")

report = Path("notes", "monday.txt").with_suffix(".md")
print(report, report.parent)
