#!/usr/bin/python3
"""My Square module"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Create a square

        Args:
            size: length of a side
        """
        self.__size = size

    @property
    def size(self):
        """Property getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size

        Args:
            value: length of a side

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square using #"""
        if self.__size == 0:
            print()

        y = self.__size
        while y > 0:
            x = self.__size
            while x > 0:
                print("#", end="\n" if x == 1 else "")
                x = x - 1
            y = y - 1
