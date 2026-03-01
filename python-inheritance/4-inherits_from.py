#!/usr/bin/python3
"""
Module that provides inheritance checking functionality.
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a subclass of a_class.

    The function returns False if obj is exactly an instance
    of a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
