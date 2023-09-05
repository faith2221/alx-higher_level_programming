#!/usr/bin/python3
"""Print the alphabet in lowercase, not followed by a new line."""
for lowercase_letter in range(97, 123):
    print("{}".format(chr(lowercase_letter)), end="")
