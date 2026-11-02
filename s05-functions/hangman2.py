import random


def pick_word():
    return random.choice(["python", "variable", "function", "loop"])


def show(word, guessed):
    return " ".join(c if c in guessed else "_" for c in word)


def is_new_guess(letter, guessed):
    return letter not in guessed


random.seed(3)
word = pick_word()
guessed = set()
lives = 6
while lives > 0:
    print(show(word, guessed), f"  lives: {lives}")
    letter = input("Guess a letter: ")
    if not is_new_guess(letter, guessed):
        print("You already guessed that")
        continue
    guessed.add(letter)
    if letter not in word:
        lives -= 1
    if all(c in guessed for c in word):
        print(f"You win! The word was {word}")
        break
else:
    print(f"Out of lives. The word was {word}")
