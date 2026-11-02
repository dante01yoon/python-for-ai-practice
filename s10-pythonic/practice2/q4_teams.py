from itertools import combinations

players = ["Maya", "Jordan", "Sam", "Ava"]
pairs = list(combinations(players, 2))
print(len(pairs), "possible pairs")
for a, b in pairs[:3]:
    print(a, "&", b)
