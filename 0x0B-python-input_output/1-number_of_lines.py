#!/usr/bin/python3
"""My number_of_lines module"""


def number_of_lines(filename=""):
    """Return the number of lines in a text file
    Args:
        filename: pathname of the text file to read
    """
    count = 0

    with open(filename, 'r') as f:
        for line in f:
            count += 1

    return count
