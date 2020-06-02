#!/usr/bin/python3
"""inherits_from module - no test cases needed"""


def inherits_from(obj, a_class):
    """Determine if an object inherits (directly or indirectly) from a_class

    Args:
        obj: the object we're checking
        a_class: the class we're checking for
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
