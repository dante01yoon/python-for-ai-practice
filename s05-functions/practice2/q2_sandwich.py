def make_sandwich(bread, *fillings):
    print(f"{bread} sandwich with: {', '.join(fillings)}")


def order(item, **options):
    for key, value in options.items():
        print(f"  {item} {key}: {value}")


make_sandwich("Wheat", "turkey", "cheddar", "lettuce")
order("Latte", size="large", milk="oat", shots=2)
