#!/usr/bin/python
"""
function add attribute to instance
>>> class MY():
...     pass

>>> mc = MY()
>>> add_attribute(mc, "name", "Jhon")
>>> print(mc.name)
Jhon
>>> a = "omar"
>>> add_attribute(a, "name", "Bob")
Traceback (most recent call last):
    ...
TypeError: can't add new attribute
"""


def add_attribute(obj, attribute, value):
    """fucntion to add attribute to object if itsnot a built in"""
    if isinstance(obj, (int, float, complex, list, tuple, range, str\
            , bytes, bytearray, memoryview, set, frozenset, dict, bool)):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
