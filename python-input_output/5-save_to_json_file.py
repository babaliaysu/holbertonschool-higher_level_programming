#!/usr/bin/python3
"""Module that writes an Object to a text file using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON string"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
