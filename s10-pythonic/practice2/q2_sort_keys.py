people = [("Maya", 29), ("Sam", 34), ("Ava", 29), ("Liam", 21)]
print(sorted(people, key=lambda p: (p[1], p[0])))
print(sorted(people, key=lambda p: -p[1])[0])
