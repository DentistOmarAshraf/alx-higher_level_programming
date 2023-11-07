#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0 or my_list == []:
        return None
    new_list = sorted(my_list)
    ret = new_list.pop()
    return (ret)
