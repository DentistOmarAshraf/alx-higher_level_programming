#!/usr/bin/python3
def multiple_returns(string):
    if len(string) == 0 or string == "":
        return (0, ' ')
    tup = (len(string), string[0])
    return (tup)
