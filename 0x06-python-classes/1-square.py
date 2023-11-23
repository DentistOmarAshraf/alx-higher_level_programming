#!/usr/bin/python3
"""
Again Its about square
"""


class Square:
    """Keep it Quite"""

    __size = 0

    def __init__(self, size=0):
        """Constractor function

        Args:
            param1 (self): instance
            param2 (int): size integer

        Returns:
            None: it just constract
        """

        self._Square__size = size
        Square.__size += size
