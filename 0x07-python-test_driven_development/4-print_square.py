#!/usr/bin/python3
"""

Printing Square

"""


def print_square(size):
    """
    function to print square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
