#!/usr/bin/python3
"""My to_json_string module"""

import json


def to_json_string(my_obj):
    """Return the JSON representation of an object
    Args:
        my_obj: the object to convert to JSON
    """
    my_obj_json = json.dumps(my_obj)

    return my_obj_json
