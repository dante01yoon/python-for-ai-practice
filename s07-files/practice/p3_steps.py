import csv

week = [("Mon", 8200), ("Tue", 6400), ("Wed", 10100), ("Thu", 7300), ("Fri", 9050)]
with open("steps.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["day", "steps"])
    writer.writerows(week)

with open("steps.csv", newline="") as f:
    rows = list(csv.DictReader(f))
best = max(rows, key=lambda r: int(r["steps"]))
print(f"Best day: {best['day']} with {int(best['steps']):,} steps")
