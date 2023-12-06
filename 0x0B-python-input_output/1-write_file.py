#!/usr/bin/python3
"""
Function to print
"""


def write_file(filename="", text=""):
    """
    funciton to write
    Args:
        param1(filename): file object
        param2(text): string objext
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    f.close()
