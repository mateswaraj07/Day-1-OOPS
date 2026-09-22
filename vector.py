# write a 2D Vector class
# you have 2 points in the 2D Space  X and Y
# represent them how ever you want
# then do some basic vector operations on them like add,subtarction, multiplication
# and scalar division, equality, dot product, magnitude
class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self, other):
       return self.x + other.x, self.y + other.y
    def sub(self, other):
        return self.x - other.x, self.y - other.y
    def mul(self, scalar):
        return self.x * scalar, self.y * scalar
    def div(self, scalar):
        return self.x / scalar, self.y / scalar
    def equal(self,other):
        return self.x == other.x and self.y == other.y
    def dot_prod(self,other):
        return self.x * other.x + self.y * other.y
    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
v1 = vector(3,4)
v2 = vector(2,5)
print("Addition:", v1.add(v2))
print("Subtraction:", v1.sub(v2))
print("Multiplication:", v1.mul(2))
print("Division:", v1.div(2))
print("Equality:", v1.equal(v2))
print("Dot Product:", v1.dot_prod(v2))
print("Magnitude:", v1.magnitude())