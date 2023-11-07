#!/usr/bin/python3
multiple_return = __import__('8-multiple_returns').multiple_returns

string = ""
length, first = multiple_return(string)
print("len = {:d}".format(length))
print("char = {:s}".format(first))

