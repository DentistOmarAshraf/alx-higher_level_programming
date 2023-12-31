#!/usr/bin/python3
"""
MY LIST
"""


class MyList(list):
    """
    My list Class inherted from list
    """

    def __init__(self, arr=[]):
        self.x = arr

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, arr):
        if isinstance(arr, list):
            self.__x = arr

    def print_sorted(self):
        print(sorted(self))
