#!/usr/bin/python3
"""This is about class prop an method"""


class Square:
    """class square"""


    __size = 0

    def __init__(self, size=0):
        """
        constructor function
        Args:
            param1(self): instance
            param2(size): must be int
        Return:
        None
        """
        self.size = size

    def area(self):
        """
        function return Area of square size ** 2

        Args:
            param1(self): instance
        Return: None
        """

        return self.size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        Square.__size += size
