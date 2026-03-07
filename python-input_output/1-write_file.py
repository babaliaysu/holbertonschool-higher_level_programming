#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file.
It provides a simple interface for file creation and overwriting.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of 
    characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string of text to write into the file.

    Returns:
        int: The total number of characters successfully written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
