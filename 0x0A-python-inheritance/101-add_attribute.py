#!/usr/bin/python3
"""Defines the add_attribute."""


def add_attribute(obj, attr_name, attr_value):
    """Checks if it's possible to add a new attribute to the object."""
    if hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
