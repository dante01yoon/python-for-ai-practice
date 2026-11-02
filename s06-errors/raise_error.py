# raise: stop with your own clear message
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError(f"Insufficient funds: balance is ${balance:.2f}")
    return balance - amount

print(withdraw(100, 30))
print(withdraw(100, 250))
