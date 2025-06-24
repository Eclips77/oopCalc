from calculator import Shape

class Square(Shape):
    def __init__(self,side):
        self.side = side
    
    def get_area(self):
        return self.side **2
    
    def get_perimeter(self):
        return self.side *4
  
