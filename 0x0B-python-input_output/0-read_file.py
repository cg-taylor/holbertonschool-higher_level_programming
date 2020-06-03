#!/usr/bin/python3
"""My read_file module"""


def read_file(filename=""):
    """Read a text file and print to stdout
    Args:
        filename: pathname of the file to read
    """
    with open(filename, 'r') as f:
        print(f.read(), end='')
