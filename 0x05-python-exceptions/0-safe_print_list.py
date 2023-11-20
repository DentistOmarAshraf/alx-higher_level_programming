#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    pr = 0
    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
            pr += 1
        except IndexError:
            break
        i += 1
    print("")
    return pr
