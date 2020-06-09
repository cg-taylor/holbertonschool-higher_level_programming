#!/usr/bin/python3
""" Base class """
import json
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert a list of dictionaries into a JSON string """
        if not list_dictionaries or list_dictionaries is None:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Convert a JSON string into a list of dictionaries """
        if not json_string or json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save list_objs to .json file """
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]

        with open('{}.json'.format(cls.__name__), 'w') as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_file(cls):
        """ Return a list of instances from a .json file """
        pass

    @classmethod
    def create(cls, **dictionary):
        """ Return an instance with all attributes preset """
        if cls.__name__ is Rectangle:
            new = cls(4, 4)
        elif cls.__name__ is Square:
            new = cls(4)
        else:
            new = None
        cls.update(new, **dictionary)
        return new
