from calculator import Shape
import math

class Hexagon(Shape):
    def __init__(self,side):
        super().__init__()
        self.side = side

    def get_area(self):
        area = (3 * math.sqrt(3) * self.side ** 2) / 2
        return area


    def get_perimeter(self):
        return 6 * self.side
    
    def __add__(self, other):
        if isinstance(other, Hexagon):
            total_area = self.get_area() + other.get_area()
            side = math.sqrt((2 * total_area) / (3 * math.sqrt(3)))
            return Hexagon(side)
        return super().__add__(other)
