#!/usr/bin/python3
"""Rectangle classi ucun modul."""


class Rectangle:
    """Duzbucaqli obyekti yaradir, sayini ve simvolunu idare edir."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Yeni obyekt yaradilir ve sayi artirilir."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Eni geri qaytarir."""
        return self.__width

    @width.setter
    def width(self, value):
        """Eni yoxlayib menimsedir."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Hundurluyu geri qaytarir."""
        return self.__height

    @height.setter
    def height(self, value):
        """Hundurluyu yoxlayib menimsedir."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Saheni hesablayir."""
        return self.__width * self.__height

    def perimeter(self):
        """Perimetri hesablayir."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """print_symbol ile duzbucaqli cekir."""
        if self.__width == 0 or self.__height == 0:
            return ""
        row = str(self.print_symbol) * self.__width
        rect = ((row + "\n") * self.__height)
        return rect[:-1]

    def __repr__(self):
        """eval() ucun lazim olan setiri qaytarir."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Obyekt silinende sayi azaldir ve mesaj yazir."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
