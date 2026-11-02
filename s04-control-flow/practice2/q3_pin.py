PIN = "2468"
for attempt in range(3):
    if input("PIN: ") == PIN:
        print("Welcome!")
        break
    print("Wrong PIN")
else:
    print("Card locked")
