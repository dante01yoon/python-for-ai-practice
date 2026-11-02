def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


operations = {"+": add, "-": subtract, "*": multiply}
a = float(input("First number: "))
op = input("Operation (+, -, *): ")
b = float(input("Second number: "))
print(a, op, b, "=", operations[op](a, b))
