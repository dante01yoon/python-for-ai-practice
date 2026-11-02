total = 0
while True:
    price = float(input("Price (0 to finish): $"))
    if price == 0:
        break
    total += price
print(f"Total: ${total:.2f}")
