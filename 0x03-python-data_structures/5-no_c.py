#!/usr/bin/python3
def no_c(my_string):
    result = my_string.translate({ord(num): None for num in 'cC'})
    return result

