# Mini project: number guessing game
import random

random.seed(7)  # same secret number every run while we practice; delete this line when you're done
secret = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Guess a number from 1 to 100: "))
    tries += 1
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print(f"Correct! You got it in {tries} tries")
        break
