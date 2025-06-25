from calculator import Shape
import math

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__()
        self.side1 = side1  
        self.side2 = side2 
        self.side3 = side3  

    def get_perimeter(self):
        # Total length around the triangle
        return self.side1 + self.side2 + self.side3

    def get_area(self):
        s = self.get_perimeter() / 2  # semi-perimeter
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def get_type(self):
        # Sort sides to easily compare and check Pythagorean condition
        a, b, c = sorted([self.side1, self.side2, self.side3])
        if a == b == c:
            return "Equilateral triangle"     # all sides equal
        elif a == b or b == c or a == c:
            return "Isosceles triangle"       # two sides equal
        elif abs(c**2 - (a**2 + b**2)) < 1e-5:
            return "Right triangle"           # follows Pythagorean theorem
        else:
            return "Scalene triangle"         # all sides different

    def __str__(self):
        return f"Triangle#{self.id}  Type: {self.get_type()}, Area: {self.get_area():.2f}, Perimeter: {self.get_perimeter():.2f}"

