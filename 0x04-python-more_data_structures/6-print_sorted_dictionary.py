#!/usr/bin/python3
def print_sorted_dictionary(a_dic):
    sorted_keys = sorted(a_dic)
    for i in sorted_keys:
        print("{:s}: {}".format(i, a_dic[i]))
