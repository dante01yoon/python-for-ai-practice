def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(greet("Maya"))
print(greet("Sam", "Good morning"))
print(greet(greeting="Hi", name="Jordan"))
