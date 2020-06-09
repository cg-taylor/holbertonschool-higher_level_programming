#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Define the Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor
        Args:
            size: length of the sides of the square
            x = horizontal offset for printing the square
            y = vertical offset for printing
            id = instance id #
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Print instance attributes """
        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """ Property getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Property setter for size """
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """ Internal helper method for update() """
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
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
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
