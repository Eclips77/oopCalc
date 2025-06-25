from calculator import Shape
import math

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius **2
    
    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def __add__(self, other):
        if isinstance(other, Circle):
            total_area = self.get_area() + other.get_area()
            new_radius = math.sqrt(total_area / math.pi)
            return Circle(new_radius)
        return super().__add__(other)