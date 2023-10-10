#!/usr/bin/pyhon3
"""Defines a function that reads a text file and prints to stdout."""


def read_file(filename=""):
    """Returns the text file to stdout."""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
