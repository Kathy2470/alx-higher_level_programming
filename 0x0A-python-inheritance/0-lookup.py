#!/usr/bin/python3
"""Defines an object attribute lookup function."""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    - obj: The object to inspect.

    Returns:
    - A list containing the names of attributes and methods.
    """
    return dir(obj)
