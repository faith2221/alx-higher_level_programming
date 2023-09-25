#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        result = 0
        for elem in my_list:
            if result < x:
                print(elem, end='')
                result += 1
        print()
        return result
    except TypeError:
        print("An error occurred. Please provide a valid list.")
        return 0
