def f_to_c(f):
    return (f - 32) * 5 / 9


def c_to_f(c):
    return c * 9 / 5 + 32


def menu():
    choice = input("1) °F to °C  2) °C to °F: ")
    value = float(input("Temperature: "))
    if choice == "1":
        print(f"{value}°F = {f_to_c(value):.1f}°C")
    else:
        print(f"{value}°C = {c_to_f(value):.1f}°F")


menu()
