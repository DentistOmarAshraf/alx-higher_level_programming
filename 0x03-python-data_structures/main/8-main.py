#!/usr/bin/python3
multiple_return = __import__('8-multiple_return').multiple_return

string = "At school, I learnt C!"
length, first = multiple_return(string)
print("len = {:d}".format(length))
print("char = {:s}".format(first))
