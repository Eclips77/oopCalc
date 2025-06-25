from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side
    
    def __add__(self, other):
        if isinstance(other, Square):
            total_area = self.get_area() + other.get_area()
            new_side = total_area ** 0.5
            return Square(new_side)
        return super().__add__(other) 

