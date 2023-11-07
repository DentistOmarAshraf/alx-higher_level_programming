#!/usr/bin/python3
def multiple_return(string):
    if string is None:
        return (0, )
    tup = (len(string), string[0])
    return (tup)
