class Rectangle:
    sides = 4

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


room = Rectangle(12, 10)
print(room.area, "square feet")
room.width = 15
print(room.area, "square feet")
print(Rectangle.sides)
