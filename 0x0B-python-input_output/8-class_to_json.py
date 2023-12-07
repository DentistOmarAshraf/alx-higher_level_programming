#!/usr/bin/python3
"""
function to return instance attributes __dict__
"""


def class_to_json(obj):
    if hasattr(obj, '__dict__'):
        return obj.__dict__
