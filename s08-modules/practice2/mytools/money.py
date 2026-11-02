def usd(amount):
    return f"${amount:,.2f}"


def add_tax(amount, rate=0.0725):
    return round(amount * (1 + rate), 2)
