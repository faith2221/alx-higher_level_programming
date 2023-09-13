#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    if not isinstance(roman_string, str):
        return 0

    prev = 0
    for symbol in reversed(roman_string):
        value = rom_dic.get(symbol, 0)
        if value < prev:
            res -= value
        else:
            res += value
        prev = value
    return res
