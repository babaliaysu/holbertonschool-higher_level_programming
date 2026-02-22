#!/usr/bin/python3
"""This module provides a function to print a formatted name.

The module validates if the inputs are strings before printing
the final "My name is <first name> <last name>" message.
"""


def say_my_name(first_name, last_name=""):
    """Prints a name in the format: My name is <first_name> <last_name>.

    Args:
        first_name (str): The first name.
        last_name (str): The last name, defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
