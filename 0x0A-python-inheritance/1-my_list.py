#!/usr/bin/python3
"""Defines MyList class."""


class MyList(list):
    """Implements MyList that prints a sorted list."""
    def append(self, value):
        """Overrides the append method to sort the list after each append."""
        super().append(value)
        self.sort()

    def print_sorted(self):
        """Prints the sorted list."""
        print(self)
