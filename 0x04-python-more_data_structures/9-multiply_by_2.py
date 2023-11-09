#!/usr/bin/python3
def multiply_by_2(a_dic):
    x = sorted(a_dic)
    new = {}
    for i in x:
        new[i] = a_dic[i] * 2
    return new
