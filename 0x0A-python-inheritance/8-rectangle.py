#!/usr/bin/python3
"""BaseGeometry module - no test cases needed"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define subclass Rectangle, which inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize private instance attributes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
