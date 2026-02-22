#!/usr/bin/python3
"""Module that defines a Square class with size and position."""


class Square:
    """A class that represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation.
        Must be a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with # and spaces for position."""
        if self.__size == 0:
            print("")
            return

        # Yuxarıdan boşluq (Vertical space)
        [print("") for i in range(self.__position[1])]

        # Kvadratı çap et (Square with horizontal space)
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
