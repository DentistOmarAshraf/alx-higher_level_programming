#!/usr/bin/python3
"""It still About Fckin Square"""


class Square:
    """Class Square"""

    __size = 0

    def __init__(self, size=0):
        """Constractor Func

        Args:
            param1 (self): object instanc
            param2 (size): int type
        Return:
            None: construction
        """
        if not isinstance(size, int):
            try:
                raise TypeError("size must be an integer")
            except TypeError as e:
                print(e)
                exit(1)
        if size < 0:
            try:
                raise ValueError("size must be >= 0")
            except ValueError as e:
                print(e)
                exit(1)

        self._Square__size = size
        Square.__size += size

    def area(self):
        """function to return the instance var (size)

        Args:
            param1(self): refer to instance

        Return:
            int: the size of square
        """
        if self._Square__size is not None:
            return self._Square__size
