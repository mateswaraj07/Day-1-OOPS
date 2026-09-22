class Rectangle:
    def __init__(self, x, y, width, height):
        #This is called ENCAPSULATION where we put all data 
        # that we need to represent a Rect in a class called Rectangle
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    #Talk about methods and class data
    def get_area(self):
         return self.width * self.height


# Create an object
r1 = Rectangle(10, 20, 50, 30)

print("Area:", r1.get_area())