balance = 100.0
DAILY_LIMIT = 500


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > DAILY_LIMIT:
        raise ValueError(f"Daily limit is ${DAILY_LIMIT}")
    if amount > balance:
        raise ValueError(f"Insufficient funds: balance is ${balance:.2f}")
    return balance - amount


while True:
    choice = input("(d)eposit, (w)ithdraw, (b)alance, (q)uit: ")
    if choice == "q":
        break
    if choice == "b":
        print(f"Balance: ${balance:.2f}")
        continue
    try:
        amount = float(input("Amount: $"))
        if choice == "d":
            if amount <= 0:
                raise ValueError("Amount must be positive")
            balance += amount
        elif choice == "w":
            balance = withdraw(balance, amount)
        print(f"Balance: ${balance:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
print("Goodbye")
