#!/usr/bin/python3
"""Square module for OOP practice."""


class Square:
    """A class that defines a square shape."""

    def __init__(self, size):
        """Constructor to set the initial dimensions.
        
        Args:
            size (int): The length of a side of the square.
        """
        self.__size = size
