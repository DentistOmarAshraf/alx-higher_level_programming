#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    while(True):
        try:
            idx = new_list.index(search)
            new_list[idx] = replace
        except ValueError:
            break
    return new_list
