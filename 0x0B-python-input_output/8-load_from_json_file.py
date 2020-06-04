#!/usr/bin/python3
"""My load_from_json_file module"""

import json


def load_from_json_file(filename):
    """Create an object from a "JSON file"
    Args:
        filename: pathname of the JSON file
    """
    with open(filename, 'r') as f:
        my_obj = json.loads(f.read())

    return my_obj
