#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """A class that represents a square."""

    def __init__(self, size=0):
        """Initialize the square."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with #."""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
