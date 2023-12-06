#!/usr/bin/python3
"""
function return from Json to Object
"""


def from_json_string(my_str):
    """function that convert from JSON to python object"""
    import json
    return json.loads(my_str)
