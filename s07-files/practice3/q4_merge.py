from pathlib import Path

with open("all_notes.txt", "w") as out:
    for path in sorted(Path("notes").glob("*.txt")):
        out.write(f"## {path.stem.title()}\n")
        out.write(path.read_text() + "\n")
print(Path("all_notes.txt").read_text())
