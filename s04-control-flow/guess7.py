import random

random.seed(7)
secret = random.randint(1, 100)

for tries in range(1, 8):
    guess = int(input(f"Guess {tries} of 7: "))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print(f"Correct! You got it in {tries} tries")
        break
else:
    print(f"Out of tries. The number was {secret}.")
