class ShapeValidator:
    @staticmethod
    def is_valid_square(width, height):
        return width > 0 and height > 0 and width == height

    @staticmethod
    def is_valid_rectangle(width, height):
        return width > 0 and height > 0

    @staticmethod
    def is_valid_circle(radius):
        return radius > 0

    @staticmethod
    def is_valid_triangle(side1, side2, side3):
        return (
            side1 > 0 and side2 > 0 and side3 > 0 and
            side1 + side2 > side3 and
            side1 + side3 > side2 and
            side2 + side3 > side1
        )

    @staticmethod
    def is_valid_hexagon(side_length):
        return side_length > 0
