from pathlib import Path

for number, path in enumerate(sorted(Path("photos").glob("IMG_*.jpg")), start=1):
    new = path.with_name(f"yosemite-{number:03}.jpg")
    path.rename(new)
    print(path.name, "->", new.name)
