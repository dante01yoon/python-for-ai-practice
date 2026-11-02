from pathlib import Path

for path in sorted(Path("notes").glob("*.txt")):
    lines = path.read_text().splitlines()
    print(f"{path.name:<15} {len(lines)} lines, {path.stat().st_size} bytes")
