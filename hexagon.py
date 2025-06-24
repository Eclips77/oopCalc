from calculator import Shape
import math

class Hexagon(Shape):
    def __init__(self,side):
        self.side = side

    def get_area(self):
        area = (3 * math.sqrt(3) * self.side ** 2) / 2
        return area


    def get_perimeter(self):
        return 6 * self.side