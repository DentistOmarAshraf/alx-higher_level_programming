#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if my_list:
        if idx < 0 or idx > len(my_list) - 1:
            for item in my_list:
                new_list.append(item)
            return new_list
        for i in range(0, len(my_list)):
            if i == idx:
                new_list.append(element)
                continue
            new_list.append(my_list[i])
        return new_list
