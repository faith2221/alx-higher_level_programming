#!/usr/bin/python3
"""Defines a child class called MyInt."""


class MyInt(int):
    """Implements MyInt which inherits from int."""
    def __eq__(self, value):
        """Overrides the equality (==) operator to invert its behaviour."""
        return self.real != value

    def __ne__(self, value):
        """Overrides the inequality (!=) operator to invert its behaviour."""
        return self.real == value
