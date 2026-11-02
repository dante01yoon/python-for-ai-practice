prices = {"coffee": 4.50, "bagel": 2.75}
item = input("Item: ")
try:
    print(f"${prices[item]:.2f}")
except KeyError:
    print(f"Sorry, we don't sell {item}.")
