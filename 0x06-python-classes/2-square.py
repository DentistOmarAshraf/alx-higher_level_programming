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
        try:
            x = size + 0
        except TypeError:
            print("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self._Square__size = size
        Square.__size += size
