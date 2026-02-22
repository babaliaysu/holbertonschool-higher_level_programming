#!/usr/bin/python3
"""This module contains the function say_my_name.

The module provides a way to print a formatted string containing
a first name and a last name, while validating the input types.
"""


def say_my_name(ad, soyad=""):
    """Prints a string with the provided first and last name.

    Args:
        ad (str): The first name to be printed.
        soyad (str): The last name to be printed. Defaults to "".

    Raises:
        TypeError: If either ad or soyad is not a string.
    """
    if not isinstance(ad, str):
        raise TypeError("first_name must be a string")

    if not isinstance(soyad, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(ad, soyad))
