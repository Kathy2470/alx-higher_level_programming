#!/usr/bin/python3

class BaseGeometry:
    """
    BaseGeometry class with public instance methods area() and integer_validator().
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value:
        - Raises a TypeError if value is not an integer with the message '<name> must be an integer'.
        - Raises a ValueError if value is less than or equal to 0 with the message '<name> must be greater than 0'.

        Args:
        - name: A string representing the name of the value.
        - value: The value to be validated.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
