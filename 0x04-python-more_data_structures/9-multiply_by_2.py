#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    res = list(new_dic.keys())
    for i in res:
        new_dic[i] *= 2
    return new_dic
