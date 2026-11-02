# try / except: keep the program running when something goes wrong
while True:
    text = input("How many tickets? ")
    try:
        tickets = int(text)
        break
    except ValueError:
        print(f"'{text}' isn't a whole number. Try again.")
print(f"Booking {tickets} tickets")
