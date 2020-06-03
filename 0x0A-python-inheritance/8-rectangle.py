#!/usr/bin/python3
"""BaseGeometry module - no test cases needed"""


class BaseGeometry:
    """Define a base class called BaseGeometry"""

    def area(self):
        """Calculate area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Determines if value is an integer

        Args:
            name: the name of the variable, always a string
            value: the value of the variable

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """Define subclass Rectangle, which inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize private instance attributes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
