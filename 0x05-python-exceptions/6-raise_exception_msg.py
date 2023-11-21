#!/usr/bin/python3
def raise_exception(msg=""):
    if msg == None or len(msg) == 0:
        msg = ""
    raise NameError(msg)
