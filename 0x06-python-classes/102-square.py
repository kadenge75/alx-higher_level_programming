#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        if isinstance(other, Square):
            return self.area() != other.area()
        return True

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False

# Example usage
if __name__ == "__main__":
    square1 = Square(5)
    square2 = Square(3)

    print("Area of square1:", square1.area())  # Output: 25
    print("Area of square2:", square2.area())  # Output: 9

    print("Is square1 equal to square2?", square1 == square2)  # Output: False
    print("Is square1 not equal to square2?", square1 != square2)  # Output: True
    print("Is square1 greater than square2?", square1 > square2)  # Output: True
    print("Is square1 greater than or equal to square2?", square1 >= square2)  # Output: True
    print("Is square1 less than square2?", square1 < square2)  # Output: False
    print("Is square1 less than or equal to square2?", square1 <= square2)  # Output: False
