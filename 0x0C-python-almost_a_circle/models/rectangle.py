#!/usr/bin/python3
""" Rectangle module """
from models.base import Base


class Rectangle(Base):
    """ Define Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor
        Args:
            width: width of the Rectangle
            height: height of the Rectangle
            x: horizontal offset from the left edge of the window; default == 0
            y: vertical offset from the current line; default == 0
            id: id number of the Rectangle; default == None
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Property gettery for width """
        return self.__width

    @property
    def height(self):
        """ Property getter for height """
        return self.__height

    @property
    def x(self):
        """ Property getter for x """
        return self.__x

    @property
    def y(self):
        """ Property getter for y """
        return self.__y

    @width.setter
    def width(self, value):
        """ Property setter for width
        Args:
            value: width of the Rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if width <= 0
        """
        if isinstance(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @height.setter
    def height(self, value):
        """ Property setter for height
        Args:
            value: height of the Rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if width <= 0
        """
        if isinstance(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @x.setter
    def x(self, value):
        """ Property setter for x
        Args:
            value: horizontal offset for printing Rectangle

        Raises:
            TypeError: if x is not an integer
            ValueError: if x is less than 0
        """
        if isinstance(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @y.setter
    def y(self, value):
        """ Property setter for y
        Args:
            value: vertical offset for printing Rectangle

        Raises:
            TypeError: if y is not an integer
            ValueError: if y is less than 0
        """
        if isinstance(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')

        self.__y = value
