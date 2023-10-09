#!/usr/bin/python3
"""Defines MyList class."""


class MyList(list):
    """Implements MyList that prints a sorted list."""
    def print_sorted(self):
        """Prints the sorted list."""
        print(sorted(self))
