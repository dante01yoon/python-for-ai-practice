def area(width, length):
    return width * length


def show_area(width, length):
    print(width * length)


rooms = [(12, 14), (10, 11), (8, 9)]
total = 0
for width, length in rooms:
    total += area(width, length)
print("Total:", total, "square feet")
print(show_area(12, 14))
