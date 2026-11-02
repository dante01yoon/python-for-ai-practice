year = int(input("Year: "))
if year % 400 == 0:
    leap = True
elif year % 100 == 0:
    leap = False
else:
    leap = year % 4 == 0
print(year, "is a leap year" if leap else "is not a leap year")
