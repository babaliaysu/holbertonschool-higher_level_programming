#!/usr/bin/python3
"""Module that defines a Square class with getter and setter."""


class Square:
    """A class that represents a square."""

    def __init__(self, size=0):
        """Initialize the square with an optional size.

        Args:
            size (int): The side length of the square.
        """
        self.size = size  # This calls the setter method directly

    @property
    def size(self):
        """Property to retrieve the private size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to set the private size attribute.

        Args:
            value (int): The value to set as size.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size
