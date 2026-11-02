def shout(text):
    return text.upper()


say = shout
print(say("hello"))

players = [("Maya", 18), ("Jordan", 21), ("Sam", 15)]
by_score = sorted(players, key=lambda p: p[1], reverse=True)
print(by_score)
