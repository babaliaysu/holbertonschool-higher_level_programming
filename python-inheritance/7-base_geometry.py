#!/usr/bin/python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """A base class for geometry-related classes."""

    def area(self):
        """Raise an Exception - subclasses must implement area().

        >>> bg = BaseGeometry()
        >>> bg.area()
        Traceback (most recent call last):
        ...
        Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        >>> bg = BaseGeometry()
        >>> bg.integer_validator("age")
        Traceback (most recent call last):
        ...
        TypeError: ...missing 1 required positional argument: 'value'
        >>> bg.integer_validator("age", 1)
        >>> bg.integer_validator("age", 0)
        Traceback (most recent call last):
        ...
        ValueError: age must be greater than 0
        >>> bg.integer_validator("age", -4)
        Traceback (most recent call last):
        ...
        ValueError: age must be greater than 0
        >>> bg.integer_validator("age", "4")
        Traceback (most recent call last):
        ...
        TypeError: age must be an integer
        >>> bg.integer_validator("age", (4,))
        Traceback (most recent call last):
        ...
        TypeError: age must be an integer
        >>> bg.integer_validator("age", [3])
        Traceback (most recent call last):
        ...
        TypeError: age must be an integer
        >>> bg.integer_validator("age", True)
        Traceback (most recent call last):
        ...
        TypeError: age must be an integer
        >>> bg.integer_validator("age", {3, 4})
        Traceback (most recent call last):
        ...
        TypeError: age must be an integer
        >>> bg.integer_validator("age", None)
        Traceback (most recent call last):
        ...
        TypeError: age must be an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
