#!/usr/bin/python3
"""A module for Square"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """Initialize a square with a specific size.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.__size = size
    @property
    def size(self):
        """Getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for zise.

        Args:
            Value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        self.__validate_size(value)
        self.__size = value
    
    def __validate_size(self, value):
        """Validate the size attribute."""
        if not isinstance(self.__size, int):
            raise TypeError("Size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
