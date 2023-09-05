#!/usr/bin/python3
for lowercase_letter in range(97, 123):
    if chr(lowercase_letter) != "q" and chr(lowercase_letter) != "e":
        print("{}".format(chr(lowercase_letter)), end="")
