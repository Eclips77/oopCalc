from input_hendler import ShapeInputHandler

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

        shape = None

        if choice == "1":
            shape = ShapeInputHandler.handle_square()
        elif choice == "2":
            shape = ShapeInputHandler.handle_rectangle()
        elif choice == "3":
            shape = ShapeInputHandler.handle_circle()
        elif choice == "4":
            shape = ShapeInputHandler.handle_triangle()
        elif choice == "5":
            shape = ShapeInputHandler.handle_hexagon()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        if shape:
            print(shape)

if __name__ == "__main__":
    main()
