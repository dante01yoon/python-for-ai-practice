class InsufficientFunds(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFunds(f"Need ${amount - balance:.2f} more")
    return balance - amount


try:
    withdraw(50, 80)
except InsufficientFunds as e:
    print("Sorry:", e)
