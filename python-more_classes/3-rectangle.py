#!/usr/bin/python3
"""Rectangle klası üçün modul"""

class Rectangle:
    """Düzbucaqlını təmsil edən klas"""

    def __init__(self, width=0, height=0):
        """Yeni bir düzbucaqlı yaradır"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Eni geri qaytarır (Getter)"""
        return self.__width

    @width.setter
    def width(self, value):
        """Eni təyin edir (Setter)"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Hündürlüyü geri qaytarır (Getter)"""
        return self.__height

    @height.setter
    def height(self, value):
        """Hündürlüyü təyin edir (Setter)"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Sahəni hesablayır"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimetri hesablayır"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Düzbucaqlını # simvolu ilə string formatında qaytarır"""
        if self.__width == 0 or self.__height == 0:
            return ""

        # Hər sətri '#' simvollarından ibarət olan siyahı yaradırıq
        rect_lines = [("#" * self.__width) for _ in range(self.__height)]
        # Sətirləri yeni sətir (\n) ilə birləşdiririk
        return "\n".join(rect_lines)
