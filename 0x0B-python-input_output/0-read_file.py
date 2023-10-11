#!/usr/bin/python3
"""Defines a function that reads a text file and prints to stdout."""


def read_file(filename=""):
    """Returns the text file to stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
