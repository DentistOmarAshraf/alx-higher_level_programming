#!/usr/bin/python3
"""
function to read from Json file and converting it to object
"""


def load_from_json_file(filename):
    """function to get json"""
    import json
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
