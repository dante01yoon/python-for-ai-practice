import csv
from collections import defaultdict

totals: defaultdict[str, float] = defaultdict(float)
with open("sales.csv", newline="") as f:
    for row in csv.DictReader(f):
        totals[row["region"]] += float(row["amount"])

for region, total in sorted(totals.items(), key=lambda item: item[1], reverse=True):
    print(f"{region:<12}${total:>9,.2f}")
