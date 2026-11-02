# Parameters: defaults and keyword arguments
def order(drink, size="medium", milk="whole"):
    return f"A {size} {drink} with {milk} milk"

print(order("latte"))
print(order("latte", "large"))
print(order("latte", milk="oat"))
