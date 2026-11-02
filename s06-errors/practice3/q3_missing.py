from pathlib import Path

name = input("File to open: ")
try:
    text = Path(name).read_text()
    print(len(text.split()), "words")
except FileNotFoundError:
    print(f"There is no file called {name!r} here.")
