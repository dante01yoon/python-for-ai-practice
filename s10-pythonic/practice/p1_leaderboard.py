players = ["Maya", "Jordan", "Sam"]
scores = [18, 21, 15]

for rank, (name, score) in enumerate(sorted(zip(players, scores), key=lambda p: p[1], reverse=True), start=1):
    print(f"{rank}. {name:<7} {score}")
