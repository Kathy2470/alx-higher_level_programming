#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""


class BaseGeometry:
    """Represent a rectangle using BaseGeometry."""

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value:

        Args:
        - name: A string representing the name of the value.
        - value: The value to be validated.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.

        Args:
        - width: The width of the rectangle.
        - height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
