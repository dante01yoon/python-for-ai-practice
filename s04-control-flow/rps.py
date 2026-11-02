# Mini project: rock paper scissors
import random

choices = ["rock", "paper", "scissors"]
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}  # the key beats the value

while True:
    me = input("rock/paper/scissors (q to quit): ")
    if me == "q":
        break
    if me not in choices:
        print("Please type rock, paper, or scissors")
        continue
    computer = random.choice(choices)
    print(f"Computer: {computer}")
    if me == computer:
        print("It's a tie")
    elif beats[me] == computer:
        print("You win!")
    else:
        print("You lose")
