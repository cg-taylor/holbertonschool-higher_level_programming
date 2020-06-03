#!/usr/bin/python3
"""BaseGeometry module - no test cases needed"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define subclass Square, which inherits from Rectangle"""

    def __init__(self, size):
        """Initialize new instance of Square

        Args:
            size: the length of each side of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of a square"""
        return self.__size ** 2
