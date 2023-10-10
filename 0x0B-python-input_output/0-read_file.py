#!/usr/bin/pyhon3
"""Defines a function that reads a text file and prints to stdout."""


def read_file(filename=""):
    """
    param filename: The name of the file to read (default is an empty string)
    """
    try:
        with open(filename, encoding='utf-8') as file:
            print(file.read(), end="")
    except FileNotFoundError:
        pass
