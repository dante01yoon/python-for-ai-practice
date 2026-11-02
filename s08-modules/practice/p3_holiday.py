from datetime import date

today = date(2026, 11, 1)
july_4 = date(2027, 7, 4)
print("Days until July 4th:", (july_4 - today).days)
print(july_4.strftime("%A, %B %d, %Y"))
