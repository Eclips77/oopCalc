from calculator import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def __add__(self, other):
        if isinstance(other, Rectangle):
            total_area = self.get_area() + other.get_area()
            ratio = self.height / self.width 
            new_width = (total_area / ratio) ** 0.5
            new_height = new_width * ratio
            return Rectangle(new_height, new_width)
        return super().__add__(other)

