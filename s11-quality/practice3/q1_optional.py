def find_price(menu: dict[str, float], item: str) -> float | None:
    return menu.get(item)


price = find_price({"coffee": 3.5}, "tea")
print(price * 2 if price is not None else "not on the menu")
