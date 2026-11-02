# Loops: the code we type line by line in the lesson
for i in range(1, 4):
    print("Hello number", i)

fruits = ["apple", "mango", "grape"]
for fruit in fruits:
    print(fruit)

count = 3
while count > 0:
    print(count)
    count = count - 1
print("Liftoff!")

while True:
    word = input("Word (q to quit): ")
    if word == "q":
        break
    print(word * 2)
