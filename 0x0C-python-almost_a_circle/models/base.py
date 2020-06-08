#!/usr/bin/python3
"""Base module"""


class Base:
    """Manage the `id` attribute"""
    __nb_objects = 0

    def __init(self, id=None):
        """Class constructor

        Args:
            id: object id number
        """
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
