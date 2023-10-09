#!/usr/bin/python3
"""Defines the add_attribute."""


def add_attribute(obj, att, value):
    """Checks if it's possible to add a new attribute to the object."""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
