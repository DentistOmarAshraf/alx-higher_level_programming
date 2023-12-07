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
    ne = []
    for i in range(len(arr)):
        ne.append(arr[i])
        if search_str in arr[i]:
            ne.append(new_str)

    with open(filename, "w", encoding="utf-8") as f:
        for i in ne:
            f.write(i)
