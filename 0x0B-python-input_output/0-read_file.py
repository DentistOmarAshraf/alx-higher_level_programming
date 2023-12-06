#!/usr/bin/python3
"""
Function to Read Module
"""


def read_file(filename=""):
    """
    Funciton to read from file
    Args:
        param1(filename): file name
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()
        print(data, end="")
