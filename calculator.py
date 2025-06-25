from abc import ABC, abstractmethod

class Shape(ABC):

    _id_counter = 1

    def __init__(self):
        self.id = Shape._id_counter
        Shape._id_counter +=1

    # Abstract method to calculate area 
    @abstractmethod
    def get_area(self):
        pass

    # Abstract method to calculate perimeter 
    @abstractmethod
    def get_perimeter(self):
        pass

    # Enables the use of '+' to sum the areas of two shapes
    def __add__(self, other):
        if isinstance(other, Shape):
            return self.get_area() + other.get_area()
        raise TypeError("Only shapes can be added together")

    # Enables the use of '-' to subtract the area of one shape from another
    def __sub__(self, other):
        if isinstance(other, Shape):
            return self.get_area() - other.get_area()
        raise TypeError("Only shapes can be subtracted")

    # Enables the use of '*' to scale the area of a shape by a number
    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return self.get_area() * factor
        raise TypeError("Can only multiply shape by a number")

    # Enables the use of '/' to divide the area of a shape by a number
    def __truediv__(self, factor):
        if isinstance(factor, (int, float)):
            return self.get_area() / factor
        raise TypeError("Can only divide shape by a number")

    # Enables '==' to compare shapes by their area
    def __eq__(self, other):
        return isinstance(other, Shape) and self.get_area() == other.get_area()

    # Enables '<' to compare shapes by area (less than)
    def __lt__(self, other):
        return isinstance(other, Shape) and self.get_area() < other.get_area()

    # Enables '<=' to compare shapes by area (less than or equal)
    def __le__(self, other):
        return isinstance(other, Shape) and self.get_area() <= other.get_area()

    # Enables '>' to compare shapes by area (greater than)
    def __gt__(self, other):
        return isinstance(other, Shape) and self.get_area() > other.get_area()

    # Enables '>=' to compare shapes by area (greater than or equal)
    def __ge__(self, other):
        return isinstance(other, Shape) and self.get_area() >= other.get_area()

    # Returns a user-friendly string representation of the shape
    def __str__(self):
        return f"{self.__class__.__name__} #{self.id}:  Area: {self.get_area():.2f}, Perimeter: {self.get_perimeter():.2f}"

    # Returns a developer-friendly representation of the shape
    def __repr__(self):
        return f"{self.__class__.__name__} #{self.id}: (area={self.get_area():.2f}, perimeter={self.get_perimeter():.2f})"

    # Returns the absolute value of the shape’s area 
    def __abs__(self):
        return abs(self.get_area())

    # Returns the perimeter as an integer when using len()
    def __len__(self):
        return int(self.get_perimeter())

    # Returns True if the shape has a positive area (used in boolean context)
    def __bool__(self):
        return self.get_area() > 0
