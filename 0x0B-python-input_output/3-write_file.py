#!/usr/bin/python3
"""My write_file module"""


def write_file(filename="", text=""):
    """Write a string to a text file and return the number of bytes written
    Args:
        filename: pathname of the file to write to
        text: string to write to the file
    """
    with open(filename, 'w') as f:
        # does not handle a non-string value passed as text
        num_write = f.write(text)
    return num_write
