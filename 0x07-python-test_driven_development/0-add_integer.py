#!/usr/bin/python3
"""

This is Add integer fucntion module

"""


def add_integer(a, b=98):
    """
    fucntion to add two integer
    """

    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    return int(a + b)
