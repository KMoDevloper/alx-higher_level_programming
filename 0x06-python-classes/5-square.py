#!/usr/bin/python3
"""A module for Square"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """Initialize a square with a specific size.

        Args:
            size (int): The size of the Square (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        """Getter method for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculate and return the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
