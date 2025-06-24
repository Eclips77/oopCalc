from validator import ShapeValidator
from square import Square
from rectangle import Rectangle
from circle import Circle
from triangle import Triangle
from hexagon import Hexagon

def main():
    while True:
        print("\nChoose a shape:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Triangle")
        print("5. Hexagon")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            width = float(input("Enter first side: "))
            height = float(input("Enter second side: "))
            if ShapeValidator.is_valid_square(width, height):
                shape = Square(width)
                print(shape)
            else:
                print("Invalid square. Sides must be equal and positive.")

        elif choice == "2":
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            if ShapeValidator.is_valid_rectangle(width, height):
                shape = Rectangle(width, height)
                print(shape)
            else:
                print("Invalid rectangle. Dimensions must be positive.")

        elif choice == "3":
            radius = float(input("Enter radius: "))
            if ShapeValidator.is_valid_circle(radius):
                shape = Circle(radius)
                print(shape)
            else:
                print("Invalid circle. Radius must be positive.")

        elif choice == "4":
            side1 = float(input("Enter first side: "))
            side2 = float(input("Enter second side: "))
            side3 = float(input("Enter third side: "))
            if ShapeValidator.is_valid_triangle(side1, side2, side3):
                shape = Triangle(side1, side2, side3)
                print(shape)
            else:
                print("Invalid triangle. Check triangle inequality rule.")

        elif choice == "5":
            side = float(input("Enter side length: "))
            if ShapeValidator.is_valid_hexagon(side):
                shape = Hexagon(side)
                print(shape)
            else:
                print("Invalid hexagon. Side must be positive.")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
