#!/usr/bin/python3
"""
function add attribute to instance
>>> class MY():
...     slots = ["first_name"]
...     pass

>>> mc = MY()
>>> add_attribute(mc, "name", "Jhon")
>>> print(mc.name)
Jhon
>>> a = "omar"
>>> add_attribute(a, "name", "Bob")
Traceback (most recent call last):
    ...
TypeError: can\'t add new attribute
>>> a = 89
>>> add_attribute(a, "name", "omar")
Traceback (most recent call last):
    ...
TypeError: can\'t add new attribute
"""


def add_attribute(obj, attribute, value):
    """fucntion to add attribute to object if itsnot a built in"""
    builtin = [int, float, complex, list, tuple, range, str, bytes]
    builtin.append([bytearray, memoryview, set, frozenset, dict, bool])
    if type(obj) in builtin or obj == None:
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
