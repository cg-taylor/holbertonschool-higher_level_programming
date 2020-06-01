#!/usr/bin/python3
"""My Rectangle module"""

class Rectangle:
    """ Define a Rectangle"""

    def __init__(self, width=0, height=0):
        """Create a rectangle

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """

        self.__width = width
        self.__height = height

    @property
    def height(self):
        """Property getter for height"""
        return self.__height

    @property
    def width(self):
        """Property getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for width

        Args:
            value: width of the rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Property setter for height

        Args:
            value: height of the rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
