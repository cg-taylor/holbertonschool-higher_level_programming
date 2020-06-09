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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def int_validator(self, name, value):
        """ Validate the type and value of a variable
        Args:
            name: name of the variable - height, width, x, or y
            value: value of the variable

        Raises:
            TypeError: if the variable is not an integer
            ValueError: if height/width <= 0 or x/y < 0
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0 and name in ['width', 'height']:
            raise ValueError('{} must be > 0'.format(name))
        if value < 0 and name in ['x', 'y']:
            raise ValueError('{} must be >= 0'.format(name))

    @property
    def width(self):
        """ Property gettery for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Property setter for width
        Args:
            value: width of the Rectangle
        """
        self.int_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """ Property getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Property setter for height
        Args:
            value: height of the Rectangle
        """
        self.int_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """ Property getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Property setter for x
        Args:
            value: horizontal offset for printing Rectangle
        """
        self.int_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """ Property getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Property setter for y
        Args:
            value: vertical offset for printing Rectangle
        """
        self.int_validator('y', value)
        self.__y = value

    def area(self):
        """ Calculate area of the Rectangle """
        return self.__width * self.__height

    def display(self):
        """ Print Rectangle to stdout using # """
        print('\n' * self.__y + (' ' * self.__x + '#' * self.__width + '\n') *
              self.__height, end='')

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """ Internal helper method for update() """
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ Update instance attributes """
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """ Create a dictionary representation of the class """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
