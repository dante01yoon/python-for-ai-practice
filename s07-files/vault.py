# Mini project: a tiny password manager (practice only — never store real passwords like this)
import json
from pathlib import Path

VAULT = Path("vault.json")
vault = json.loads(VAULT.read_text()) if VAULT.exists() else {}

while True:
    cmd = input("(a)dd, (g)et, (l)ist, (q)uit: ")
    if cmd == "q":
        break
    if cmd == "a":
        site = input("Site: ")
        vault[site] = input("Password: ")
        VAULT.write_text(json.dumps(vault, indent=2))
        print(f"Saved {site}")
    elif cmd == "g":
        site = input("Site: ")
        print(vault.get(site, "Not found"))
    elif cmd == "l":
        print(", ".join(vault) or "Empty")
