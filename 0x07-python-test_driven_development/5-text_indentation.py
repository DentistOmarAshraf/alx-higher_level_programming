#!/usr/bin/python3
"""

Fucntion to print text line by line if the finshed lint is symbol

"""


def text_indentation(text):
    """
    function text_indentation
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    symb = [".", "?", ":"]
    i = 0
    while i < len(text):
        print("{:s}".format(text[i]), end="")
        if text[i] in symb:
            print("")
            print("")
            i += 1
            while (text[i + 1] == " "):
                i += 1
        i += 1
