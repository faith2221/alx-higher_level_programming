#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    res = list(a_dictionary.keys())
    res.sort()
    for i in res:
        print("{}: {}".format(i, a_dictionary.get(i)))
