#!/usr/bin/python3
"""Defines the BaseGeometry class."""


class BaseGeometry:
    """Implements the BaseGeometry."""
    def area(self):
        """Raises an Exception with a custom error message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if the value is an integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
