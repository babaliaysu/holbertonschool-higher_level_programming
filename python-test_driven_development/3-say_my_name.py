#!/usr/bin/python3
"""This module provides a function to print a formatted name.

The module validates if the inputs are strings before printing
the final "My name is <first name> <last name>" message.
"""


def say_my_name(ad, soyad=""):
    """Prints a name in the format: My name is <first_name> <last_name>.

    Args:
        ad (str): The first name.
        soyad (str): The last name, defaults to an empty string.

    Raises:
        TypeError: If ad or soyad are not strings.
    """
    if not isinstance(ad, str):
        raise TypeError("first_name must be a string")

    if not isinstance(soyad, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(ad, soyad))
