#!/usr/bin/python3
"""Prints the square."""


def print_square(size):
    """Prints a square with a character '#'."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for col in range(size):
            print("#", end='\n' if col == size - 1 else "")
