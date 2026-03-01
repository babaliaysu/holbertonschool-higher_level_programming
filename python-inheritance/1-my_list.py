#!/usr/bin/python3
"""
This module contains the MyList class.
The class inherits from the built-in list object.
"""


class MyList(list):
    """
    MyList class that provides a method to print a sorted list.
    Inherits all properties from the built-in list.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending order.
        Assumes all elements are integers.
        """
        print(sorted(self))
