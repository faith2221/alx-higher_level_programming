#!/usr/bin/python3
"""Defines is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """Checks if the object's class is a subclass of the specified class."""

    return isinstance(obj, a_class)
