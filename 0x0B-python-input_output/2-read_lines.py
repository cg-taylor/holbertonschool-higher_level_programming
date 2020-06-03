#!/usr/bin/python3
"""My read_lines module"""


def read_lines(filename="", nb_lines=0):
    """Read `nb_lines` lines of a text file and print to stdout
    Args:
        filename: pathname of the text file to read
        nb_lines: the number of lines to print; prints whole file if <= 0
            or if >= total # of lines in the file
    """
    with open(filename, 'r') as f:
        if nb_lines <= 0:
            print(f.read(), end='')

        while nb_lines > 0:
            print(f.readline(), end='')
            nb_lines -= 1
