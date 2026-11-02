import csv
from collections import defaultdict
from pathlib import Path

rows: defaultdict[str, list[dict[str, str]]] = defaultdict(list)
with open("sales.csv", newline="") as f:
    for row in csv.DictReader(f):
        rows[row["region"]].append(row)

Path("regions").mkdir(exist_ok=True)
for region, sales in rows.items():
    with open(Path("regions", f"{region.lower()}.csv"), "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "region", "amount"])
        writer.writeheader()
        writer.writerows(sales)
    print(f"{region:<10} -> regions/{region.lower()}.csv")
