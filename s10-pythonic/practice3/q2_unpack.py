scores = [98, 91, 87, 75, 60]
first, second, *rest = scores
print(first, second, rest)

names = ["Ana", "Ben", "Chloe"]
lengths = {name: len(name) for name in names}
print(lengths)
long_names = {name for name in names if len(name) > 3}
print(long_names)
