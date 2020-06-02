#!/usr/bin/python3
"""is_kind_of_class module - no test cases required"""


def is_kind_of_class(obj, a_class):
    """Determine if an object is an instance or subclass of a class

    Args:
        obj: the object we're checking
        a_class: the class we're checking for
    """
    return isinstance(obj, a_class)
