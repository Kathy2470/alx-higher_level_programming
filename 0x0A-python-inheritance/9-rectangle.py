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


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """

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

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
        - The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle in the format '[Rectangle] <width>/<height>'.

        Returns:
        - A string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
