#!/usr/bin/python3
"""
Function Return a list of all available attributes and method
"""


def lookup(obj):
    """
    lookup fucntion
    Args:
        param1(obj)
    Return:
        list of all attributes
    """
    return list(dir(obj))
