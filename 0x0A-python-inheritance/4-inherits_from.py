#!/usr/bin/python3
"""
function inherits from class
"""


def inherits_from(obj, a_class):
    """
    inherits_from function to know if it is subclass
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
