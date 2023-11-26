#!/usr/bin/python3
"""About Class prop and method, getter and setter"""


class Square:
    """Class square"""

    __size = 0

    def __init__(self, size):
        """constructor function
        Args:
            param1(self): instance
            param2(size): integer
        Return:
            None
        """

        self.size = size

    def area(self):
        """Square Area function
        Args:
            param1(self): instance
            param2(size): integer
        Return:
            None
        """

        return self.size ** 2

    def my_print(self):
        """Print Square function
        Args:
            param1(self): instance
        Return:
            NONE
        """

        if self.size == 0:
            print("")
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print("")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        Square.__size += size
