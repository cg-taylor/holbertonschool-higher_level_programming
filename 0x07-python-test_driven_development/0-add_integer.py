#!/usr/bin/python3
"""0-add_integer module"""

def add_integer(a, b=98):
    """Add two integers

    Args:
        a: the first number
        b: the second number. Defaults to 98

    Raises:
        TypeError: if a or b is not an integer
    """

    if type(a) is not [int, float]:
        raise TypeError('a must be an integer')
    elif type(a) is float:
        a = int(a)

    if type(b) is not [int, float]:
        raise TypeError('b must be an integer')
    elif type(b) is float:
        b = int(b)

    return a + b
