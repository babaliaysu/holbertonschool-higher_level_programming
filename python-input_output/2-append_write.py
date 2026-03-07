#!/usr/bin/python3
"""Module that appends a string to a text file"""


def append_write(filename="", text=""):
    """Appends a string to a UTF8 text file and returns added chars"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
