def order(item, quantity):
    menu = {"coffee": 3.50, "bagel": 2.75}
    if quantity <= 0:
        raise ValueError("quantity must be at least 1")
    return menu[item] * quantity


for item, quantity in [("coffee", 2), ("bagel", 0), ("pizza", 1)]:
    try:
        print(item, order(item, quantity))
    except ValueError as e:
        print(item, "error:", e)
    except KeyError:
        print(item, "error: not on the menu")
