# app.py
from input_hendler import ShapeInputHandler

class ShapeApp:
    def __init__(self):
        self.shapes = []

    def run(self):
        while True:
            self.print_main_menu()
            choice = input("Enter your choice: ").strip()

            match choice:
                case "1":
                    shape = self.choose_shape()
                    if shape:
                        self.shapes.append(shape)
                        print("Shape added!")
                case "2":
                    self.print_shapes()
                case "3":
                    self.compare_shapes()
                case "4":
                    self.add_shapes()
                case "5":
                    self.subtract_shapes()
                case "6":
                    self.show_max()
                case "7":
                    self.show_min()
                case "8":
                    self.divade_shapes()
                case "0":
                    print("Goodbye!")
                    break
                case _:
                    print("Invalid choice.")

    def print_main_menu(self):
        print("\nMain Menu:")
        print("1. Create new shape")
        print("2. Show all shapes")
        print("3. Compare two shapes")
        print("4. Add areas of two shapes")
        print("5. Subtract areas of two shapes")
        print("6. Show shape with largest area")
        print("7. Show shape with smallest area")
        print("8. Divide area of one shape by another")
        print("0. Exit")

    def choose_shape(self):
         print("\nChoose a shape:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Triangle")
        print("5. Hexagon")

        match input("Enter your option: ").strip():
            case "1": return ShapeInputHandler.handle_square()
            case "2": return ShapeInputHandler.handle_rectangle()
            case "3": return ShapeInputHandler.handle_circle()
            case "4": return ShapeInputHandler.handle_triangle()
            case "5": return ShapeInputHandler.handle_hexagon()
            case _: return None

    def print_shapes(self):
        if not self.shapes:
            print("No shapes yet.")
        for i, s in enumerate(self.shapes):
            print(f"{i}. {s}")

    def get_two_shapes(self):
        if len(self.shapes) < 2:
            print("Need at least two shapes.")
            return None, None
        self.print_shapes()
        try:
            i1 = int(input("Index of first: "))
            i2 = int(input("Index of second: "))
            return self.shapes[i1], self.shapes[i2]
        except:
            print("Invalid input.")
            return None, None

    def compare_shapes(self):
        s1, s2 = self.get_two_shapes()
        if s1 and s2:
            print(f"{s1} == {s2} → {s1 == s2}")
            print(f"{s1} > {s2} → {s1 > s2}")
            print(f"{s1} < {s2} → {s1 < s2}")

    def add_shapes(self):
        s1, s2 = self.get_two_shapes()
        if s1 and s2:
            print(f"Combined area: {s1 + s2:.2f}")

    def subtract_shapes(self):
        s1, s2 = self.get_two_shapes()
        if s1 and s2:
            print(f"Area difference: {s1 - s2:.2f}")

    def show_max(self):
        if self.shapes:
            print("Shape with largest area:", max(self.shapes))
        else:
            print("No shapes.")

    def show_min(self):
        if self.shapes:
            print("Shape with smallest area:", min(self.shapes))
        else:
            print("No shapes.")
    
    def divade_shapes(self):
        s1, s2 = self.get_two_shapes()
        if s1 and s2:
            try:
                print(f"Area of shape {s1.id} divided by area of shape {s2.id}: {s1.get_area() / s2.get_area():.2f}")
            except ZeroDivisionError:
                print("Cannot divide by zero area shape.")
            except TypeError as e:
                print(f"Error: {e}")
