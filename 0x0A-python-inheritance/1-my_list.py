#!/usr/bin/python3
"""MyList class module
Test cases in tests/1-my_lists.txt
"""


class MyList(list):
    """my class, MyList, inherits from list"""
    def print_sorted(self):
        """Print a list in ascending order"""
        print(sorted(self))
