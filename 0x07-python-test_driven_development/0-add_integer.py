#!/usr/bin/python3
"""It contains a function to add two integers."""


def add_integer(a, b=98):
    """Function that returns an integer and raises TypeError."""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
