#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        my_max = my_list[0]
        for num in my_list:
            if num > my_max:
                my_max = num
    return my_max
