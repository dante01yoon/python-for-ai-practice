while True:
    try:
        age = int(input("Age: "))
        break
    except ValueError:
        print("Please type a whole number, like 29.")
print(f"In 10 years, you'll be {age + 10}.")
