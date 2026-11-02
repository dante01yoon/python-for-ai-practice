import csv

rows = [
    {"category": "Rent", "amount": 1850},
    {"category": "Groceries", "amount": 420},
    {"category": "Gas", "amount": 160},
    {"category": "Streaming", "amount": 32},
]
with open("budget.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["category", "amount"])
    writer.writeheader()
    writer.writerows(rows)

with open("budget.csv", newline="") as f:
    data = [(row["category"], int(row["amount"])) for row in csv.DictReader(f)]

total = sum(amount for _, amount in data)
name, biggest = max(data, key=lambda pair: pair[1])
print(f"Total: ${total:,}")
print(f"Biggest: {name}, ${biggest:,} ({biggest / total:.0%} of the total)")
