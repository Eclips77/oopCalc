from calculator import Shape

class Square(Shape):
    def __init__(self,side):
        super().__init__("Square")
        self.side = side
    
    def get_area(self):
        return self.side **2
    
    def get_perimeter(self):
        return self.side *4
    
    def __str__(self):
        return f"{self.name} with width {self.width} and height {self.height}"
