#!/usr/bin/python3
"""
Function to append a text to file
"""


def append_write(filename="", text=""):
    """
    function to create a file if it doesnt exist
    and if it exist it append the text
    Args:
        param1(filename): file object
        param2(text): string
    """
    with open(filename, "a+", encoding="utf-8") as f:
        nb = f.write(text)
    return nb
