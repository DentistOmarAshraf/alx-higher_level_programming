#!/usr/bin/python3
"""
function append_after
"""


def append_after(filename="", search_str="", new_str=""):
    """Function to append text After certin txt"""
    arr = []
    with open(filename, "r", encoding="utf-8") as f:
        line = f.readline()
        arr.append(line)
        while line:
            line = f.readline()
            if line != '':
                arr.append(line)
    for i in range(len(arr)):
        if search_str in arr[i]:
            arr.insert(i + 1, new_str)

    with open(filename, "w", encoding="utf-8") as f:
        for i in arr:
            f.write(i)
