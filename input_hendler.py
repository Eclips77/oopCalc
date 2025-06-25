from validator import ShapeValidator
from square import Square
from rectangle import Rectangle
from circle import Circle
from triangle import Triangle
from hexagon import Hexagon

class ShapeInputHandler:
    @staticmethod
    def handle_square():
        width = float(input("Enter first side: "))
        height = float(input("Enter second side: "))
        if ShapeValidator.is_valid_square(width, height):
            return Square(width)
        else:
            print("Invalid square. Sides must be equal and positive.")
            return None

    @staticmethod
    def handle_rectangle():
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        if ShapeValidator.is_valid_rectangle(width, height):
            return Rectangle(width, height)
        else:
            print("Invalid rectangle. Dimensions must be positive.")
            return None

    @staticmethod
    def handle_circle():
        radius = float(input("Enter radius: "))
        if ShapeValidator.is_valid_circle(radius):
            return Circle(radius)
        else:
            print("Invalid circle. Radius must be positive.")
            return None

    @staticmethod
    def handle_triangle():
        side1 = float(input("Enter first side: "))
        side2 = float(input("Enter second side: "))
        side3 = float(input("Enter third side: "))
        if ShapeValidator.is_valid_triangle(side1, side2, side3):
            return Triangle(side1, side2, side3)
        else:
            print("Invalid triangle. Does not follow triangle inequality.")
            return None

    @staticmethod
    def handle_hexagon():
        side = float(input("Enter side length: "))
        if ShapeValidator.is_valid_hexagon(side):
            return Hexagon(side)
        else:
            print("Invalid hexagon. Side must be positive.")
            return None
