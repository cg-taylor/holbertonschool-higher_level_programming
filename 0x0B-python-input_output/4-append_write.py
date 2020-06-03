#!/usr/bin/python3
"""My append_write module"""


def append_write(filename="", text=""):
    """Append a string to the end of a text file, return number of bytes printed
    Args:
        filename: pathname of the file to append to
        text: string to append to the file
    """
    with open(filename, 'a') as f:
        num_append = f.write(text)

    return num_append
