items = []
while True:
    choice = input("add, list, or quit? ")
    if choice == "quit":
        break
    elif choice == "add":
        items.append(input("Item: "))
    elif choice == "list":
        print(items)
print("Bye!")
