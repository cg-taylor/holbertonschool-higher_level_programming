#!/usr/bin/python3
"""My save_to_json_file module"""

import json


def save_to_json_file(my_obj, filename):
    """Write the JSON representation of an object to a text file
    Args:
        my_obj: the object to write to the file
        filename: the name of the text file
    """
    with open(filename, 'w') as f:
        obj_json = json.dumps(my_obj)
        f.write(obj_json)
