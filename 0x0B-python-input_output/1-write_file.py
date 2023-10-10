#!/usr/bin/python3
"""Defines a function that writes to a text file."""


def write_file(filename="", text=""):
    """Writes a string to text file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
