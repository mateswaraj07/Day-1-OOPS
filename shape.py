class Shape:
    def __init__(self, color):
        self.color = color


class Rectangle(Shape):
    def __init__(self, x, y, width, height, color):
        super().__init__(color)

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


# Create Rectangle object
r1 = Rectangle(10, 20, 50, 30, "Red")

print("Color:", r1.color)
print("X:", r1.x)
print("Y:", r1.y)
print("Width:", r1.width)
print("Height:", r1.height)
print("Area:", r1.get_area())