#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for let in my_string:
        if let == "c" or let == "C":
            continue
        new += let
    return new
