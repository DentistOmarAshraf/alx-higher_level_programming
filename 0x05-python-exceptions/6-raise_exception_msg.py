#!/usr/bin/python3
def raise_exception(msg=""):
    try:
        raise TypeError(msg)
    except TypeError:
        pass
