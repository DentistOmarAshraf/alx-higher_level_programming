#!/usr/bin/python3
def best_score(a_dic):
    if a_dic is None:
        return None
    x = sorted(a_dic.items(), key=lambda item: item[1])
    return x[len(x) - 1][0]
