import hashlib
from pathlib import Path

seen: dict[str, str] = {}
for path in sorted(Path("phone").iterdir()):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest in seen:
        print(path.name, "is a copy of", seen[digest])
    else:
        seen[digest] = path.name
