# CSV: a monthly budget in dollars
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

total = 0
with open("budget.csv", newline="") as f:
    for row in csv.DictReader(f):
        print(f"{row['category']:<10} ${int(row['amount']):>5}")
        total += int(row["amount"])
print(f"{'Total':<10} ${total:>5}")
