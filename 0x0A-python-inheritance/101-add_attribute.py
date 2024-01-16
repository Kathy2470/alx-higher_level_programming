#!/usr/bin/python3
"""Defines a function that adds attribute to objects."""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Raises a TypeError exception with the message "can't add new attribute"
    if the object can't have a new attribute.

    Args:
    - obj: The object to which the attribute should be added.
    - attribute: The name of the new attribute.
    - value: The value to assign to the new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
