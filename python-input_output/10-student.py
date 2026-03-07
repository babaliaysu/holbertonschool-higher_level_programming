#!/usr/bin/python3
"""Defines a Student class with filter"""


class Student:
    """Representation of a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary of the student with filter"""
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
