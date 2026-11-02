import random


def roll(sides=6, times=1):
    return [random.randint(1, sides) for _ in range(times)]


random.seed(4)
print(roll())
print(roll(20))
print(roll(times=3))
