bill = float(input("Bill: $"))
percent = float(input("Tip %: "))
people = int(input("People: "))

tip = bill * percent / 100
total = bill + tip
print(f"Tip:   ${tip:.2f}")
print(f"Total: ${total:.2f}")
print(f"Each:  ${total / people:.2f}")
