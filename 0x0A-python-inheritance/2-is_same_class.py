#!/usr/bin/python3
"""is_same_class module - no test cases required"""


def is_same_class(obj, a_class):
    """Determine if object is exactly an instance of the given class

    Args:
        obj: the object to check
        a_class: the class we're checking fo
    """
    return type(obj) == a_class
