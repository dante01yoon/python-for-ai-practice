# pathlib: paths as objects
from pathlib import Path

folder = Path("data")
folder.mkdir(exist_ok=True)
file = folder / "hello.txt"
file.write_text("Hello from pathlib")
print(file)
print(file.exists(), file.suffix, file.stem)
print(file.read_text())
