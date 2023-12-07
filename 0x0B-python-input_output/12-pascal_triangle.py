#!/usr/bin/python3
"""

This is Tech interview prepartion Question
Its About How to return 2d array of Pascal_Triangle

"""


def pascal_triangle(x):
    """The pascal function"""
    base = 1
    new = []
    for i in range(1, x + 1):
        arr = []
        for j in range(1, i + 1):
            if j == base or j == i:
                arr.append(base)
            else:
                arr.append(pre[j - 2] + pre[j - 1])
        new.append(arr)
        pre = arr
    return new
