#!/usr/bin/python3
def remove_char_at(str, n):
    x = len(str)
    strret = ""
    for i in range(0, x):
        if i == n:
            continue
        strret += str[i]
    return (strret)
