# Mini project: Hangman
import random

def pick_word():
    return random.choice(["python", "variable", "function", "loop"])

def show(word, guessed):
    return " ".join(c if c in guessed else "_" for c in word)

random.seed(3)  # same word every run while we practice
word = pick_word()
guessed = set()
lives = 6
while lives > 0:
    print(show(word, guessed), f"  lives: {lives}")
    letter = input("Guess a letter: ")
    guessed.add(letter)
    if letter not in word:
        lives -= 1
    if all(c in guessed for c in word):
        print(f"You win! The word was {word}")
        break
else:
    print(f"Out of lives. The word was {word}")
