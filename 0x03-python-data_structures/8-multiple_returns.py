#!/usr/bin/python3
def multiple_returns(string):
    if string == "":
        return (0, None)
    tup = (len(string), string[0])
    return (tup)
