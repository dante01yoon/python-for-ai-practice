price = float(input("Price: $"))
quantity = int(input("Quantity: "))
subtotal = price * quantity
tax = subtotal * 0.0725
print(f"Subtotal: ${subtotal:,.2f}")
print(f"Tax:      ${tax:,.2f}")
print(f"Total:    ${subtotal + tax:,.2f}")
