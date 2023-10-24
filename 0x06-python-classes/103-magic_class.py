#!/usr/bin/python3
import math

class MagicClass:
    def __init__(self, radius):
        if type(radius) not in (int, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius

# Example usage
if __name__ == "__main__":
    # Create an instance of MagicClass with radius 5
    magic_circle = MagicClass(5)

    # Calculate and print the area and circumference of the circle
    print("Area of the circle:", magic_circle.area())  # Output: 78.53981633974483
    print("Circumference of the circle:", magic_circle.circumference())  # Output: 31.41592653589793
