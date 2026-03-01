#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass


class Circle(Shape):
    """Represents a circle."""

    def __init__(self, radius):
        """Initializes the circle with a radius."""
        self.__radius = radius

    def area(self):
        """Returns the area of the circle."""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Returns the perimeter of the circle."""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """Initializes the rectangle with width and height."""
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)
