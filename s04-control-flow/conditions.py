# Conditionals: the code we type line by line in the lesson
score = int(input("Your score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Keep practicing!")

command = input("Command: ")
match command:
    case "start":
        print("Starting the game")
    case "quit":
        print("Goodbye")
    case _:
        print("Unknown command")
