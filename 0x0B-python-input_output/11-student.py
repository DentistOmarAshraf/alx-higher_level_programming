#!/usr/bin/python3
"""
class Student
"""


class Student:
    """this class is student"""

    def __init__(self, first_name, last_name, age):
        """
        Constructor function
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        if attr is None:
            return self.__dict__
        dic = {}
        for item in attr:
            if item in self.__dict__:
                dic[item] = self.__dict__[item]
        return dic

    def reload_from_json(self, json):
        for item in json:
            setattr(self, item, json[item])
