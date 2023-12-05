#!/usr/bin/python3
"""
class Geometry based in task 6
"""


class BaseGeometry:
    """
    Class BaseGeometry
    """
    def area(self):
        """
        Public method
        raise exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validator function
        Args:
            param1(self): instance
            param2(name): must be string
            param3(value): must be integer & greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = name
        self.value = value
