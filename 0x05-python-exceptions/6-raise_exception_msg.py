#!/usr/bin/python3
def raise_exception(msg=""):
    raise NameError(msg)

try:
    raise_exception("C is fun")
except NameError as ne:
    print(ne)
