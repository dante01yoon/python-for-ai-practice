from pathlib import Path

word = input("Search for: ").lower()
for path in sorted(Path("notes").glob("*.txt")):
    for number, line in enumerate(path.read_text().splitlines(), start=1):
        if word in line.lower():
            print(f"{path.name}:{number}: {line}")
