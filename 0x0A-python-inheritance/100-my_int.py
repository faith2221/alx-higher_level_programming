#!/usr/bin/python3
"""Defines a child class called MyInt."""


class MyInt(int):
    """Implements MyInt which inherits from int."""
    def __init__(self, value):
        """Initializes the MyInt object with the given integer."""
        super().__init__(value)

    def __eq__(self, other):
        """Overrides the equality (==) operator to invert its behaviour."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the inequality (!=) operator to invert its behaviour."""
        return auper().__eq__(other)
