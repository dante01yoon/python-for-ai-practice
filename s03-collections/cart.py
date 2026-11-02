# Mini project: shopping cart with sales tax (California statewide base rate 7.25%)
menu = {"coffee": 4.50, "bagel": 2.75, "muffin": 3.25}
cart = []
while True:
    item = input("Add an item (or done): ")
    if item == "done":
        break
    if item in menu:
        cart.append(item)
    else:
        print("Not on the menu")
subtotal = sum(menu[i] for i in cart)
tax = subtotal * 0.0725
print(f"Items: {cart}")
print(f"Subtotal ${subtotal:.2f}, tax ${tax:.2f}, total ${subtotal + tax:.2f}")
