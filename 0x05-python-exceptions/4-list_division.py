#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new = []
    while i < list_length:
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            new.append(res)
            i += 1
    return new
