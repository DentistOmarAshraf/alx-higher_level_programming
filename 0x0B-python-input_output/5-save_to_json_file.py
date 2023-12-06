#!/usr/bin/python3
"""
Fucntion to save Json to file
"""


def save_to_json_file(my_obj, filename):
    """function to save Json to file"""
    import json
    data = json.dumps(my_obj)
    with open(filename, "a+", encoding="utf-8") as f:
        f.write(data)
