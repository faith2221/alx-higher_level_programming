#!/usr/bin/python3
"""Defines inherits_from."""


def inherits_from(obj, a_class):
    """Checks if the object's class is a subclass of the specified class."""

    return isinstance(obj, a_class) and obj.__class__ is not a_class
