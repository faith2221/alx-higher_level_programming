#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    res = 0 
    for score, weight in my_list:
        total += score * weight
        res += weight
    if res == 0:
        return 0
    return total / res
