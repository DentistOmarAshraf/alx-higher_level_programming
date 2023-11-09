#!/usr/bin/python3
def simple_delete(a_dic, key=""):
    try:
        del a_dic[key]
    except:
        pass
    return a_dic
