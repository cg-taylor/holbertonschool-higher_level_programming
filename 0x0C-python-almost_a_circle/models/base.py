#!/usr/bin/python3
""" Base class """


class Base:
    """Manage the `id` attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class instance constructor

        Args:
            id: object id number
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
