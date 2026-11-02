menu = {"coffee": 4.50, "bagel": 2.75, "muffin": 3.25}
cart = []
while True:
    item = input("Add an item (or remove, done): ")
    if item == "done":
        break
    if item == "remove":
        name = input("Remove which item? ")
        if name in cart:
            cart.remove(name)
            print(f"Removed {name}")
        else:
            print(f"{name} isn't in your cart")
    elif item in menu:
        cart.append(item)
    else:
        print("Not on the menu")
subtotal = sum(menu[i] for i in cart)
tax = subtotal * 0.0725
print(f"Items: {cart}")
print(f"Subtotal ${subtotal:.2f}, tax ${tax:.2f}, total ${subtotal + tax:.2f}")
