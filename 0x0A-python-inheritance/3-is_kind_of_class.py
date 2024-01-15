#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance or inherited instance of a class.

    Args:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - True if obj is an instance of a_class or its subclass; False otherwise.
    """
    return isinstance(obj, a_class)
