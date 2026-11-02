from datetime import date

entry = input("Today's note: ")
with open("journal.txt", "a") as f:
    f.write(f"{date.today()}: {entry}\n")

with open("journal.txt") as f:
    for number, line in enumerate(f, start=1):
        print(number, line.strip())
