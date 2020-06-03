#!/usr/bin/python3
"""My from_json_string module"""

import json


def from_json_string(my_str):
    """Return the object represented by a JSON string
    Args:
        my_str: the JSON string to convert to an object
    """
    my_obj = json.loads(my_str)

    return my_obj
