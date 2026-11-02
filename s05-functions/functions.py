# Functions: name a piece of work, then reuse it
def greet(name):
    print(f"Hi, {name}!")

greet("Maya")
greet("Jordan")


def to_celsius(f):
    return (f - 32) * 5 / 9

print(round(to_celsius(72), 1))
print(round(to_celsius(98.6), 1))
