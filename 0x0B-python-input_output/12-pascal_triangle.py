#!/usr/bin/python3
"""

This is Tech interview prepartion Question
Its About How to return 2d array of Pascal_Triangle

"""


def pascal_triangle(x):
    """The pascal function"""
    new = []
    for i in range(1, x + 1):
        arr = []
        for j in range(i):
            if j == 0 or j == i - 1:
                arr.append(1)
            else:
                arr.append(pre[j - 1] + pre[j])
        new.append(arr)
        pre = arr
    return new
