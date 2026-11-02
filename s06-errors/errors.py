# Reading errors: a traceback tells you where and why
prices = {"coffee": 4.50, "bagel": 2.75}
order = ["coffee", "muffin"]
total = 0
for item in order:
    total += prices[item]
print(total)
