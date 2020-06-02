#!/usr/bin/python3
'''My lookup module'''


def lookup(obj):
    '''Return a list of all attributes and methods of an inherited class

    Args:
        obj: the name of the parent class
    '''
    return dir(obj)
