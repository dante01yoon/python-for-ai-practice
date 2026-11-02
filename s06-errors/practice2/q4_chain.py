def parse_price(text):
    return float(text.replace("$", ""))


def total(prices):
    return sum(parse_price(p) for p in prices)


print(total(["$4.50", "$3.25", "free"]))
