def subtotal(prices):
    return sum(prices)


def discount(amount, percent):
    return amount * (1 - percent / 100)


def with_tax(amount, rate=8.25):
    return amount * (1 + rate / 100)


cart = [19.99, 5.49, 12.00]
total = with_tax(discount(subtotal(cart), 10))
print(f"Total: ${total:.2f}")
