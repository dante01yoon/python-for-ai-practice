files = ["report.csv", "photo.png", "sales.csv", "notes.txt"]

csv_files = [f for f in files if f.endswith(".csv")]
print(csv_files)

squares = [n * n for n in range(1, 6)]
print(squares)

prices = {"latte": 4.50, "bagel": 3.25}
with_tax = {name: round(price * 1.0825, 2) for name, price in prices.items()}
print(with_tax)
