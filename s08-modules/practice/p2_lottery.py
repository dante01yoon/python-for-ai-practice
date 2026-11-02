import random

random.seed(2026)
white = sorted(random.sample(range(1, 70), 5))
red = random.randint(1, 26)
print("White balls:", white, " Powerball:", red)
