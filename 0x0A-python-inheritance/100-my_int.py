#!/usr/bin/python3
"""Class int inhertance"""


class MyInt(int):
    """this class inherits the int class"""

    def __init__(self, num):
        """
        Constructor function
        """
        if type(num) != int:
            raise TypeError("num must be integer")
        self.__value = num

    def __str__(self):
        string = "{:d}".format(self.__value)
        return string

    def __eq__(self, x):
        if self.__value == x:
            return False
        return True

    def __ne__(self, x):
        if self.__value != x:
            return False
        return True
