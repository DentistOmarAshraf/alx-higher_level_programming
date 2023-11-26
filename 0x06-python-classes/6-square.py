#!/usr/bin/python3
"""Class props and method, getter and setter"""


class Square:
    """Class Square"""

    __size = 0

    def __init__(self, size=0, position=(0, 0)):
        """Constructor Function
        Args:
            param1(self): instance
            param2(size): integer
            param3(postion): tuple
        Return:
            NONE
        """

        self.size = size
        self.position = position

    def area(self):
        """Area Function
        Args:
            param1(self): instance
        Return:
            int: area of square
        """

        return self.size ** 2

    def my_print(self):
        """Print Square
        Args:
            param1(self): instance
        Return:
            None
        """

        if self.size == 0:
            print("")
        for i in range(self.position[1]):
            print("")
        for i in range(self.size):
            for n in range(self.position[0]):
                print(" ", end="")
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position=(0, 0)):
        self.__position = position
