#!/usr/bin/python3


class Rectangle:
    """Class representing a rectangle."""
    
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        self.validate_non_negative_integer("width", value)
        self.__height = value

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        self.validate_non_negative_integer("width", value)
        self.__width = value

    def validate_non_negative_integer(self, attribute, value):
        """Validate that the given value is a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        elif value < 0:
            raise ValueError(f"{attribute} must be >= 0")
