#!/usr/bin/python3
def simple_delete(a_dic, key=""):
    x = sorted(a_dic)
    if key in x:
        del a_dic[key]
    return a_dic
