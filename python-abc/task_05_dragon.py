#!/usr/bin/python3
"""Defines mixins for swimming and flying, and a Dragon class."""


class SwimMixin:
    """Mixin that adds swimming functionality."""
    def swim(self):
        """Prints swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying functionality."""
    def fly(self):
        """Prints flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A Dragon class that can swim, fly, and roar."""
    def roar(self):
        """Prints the dragon's roar."""
        print("The dragon roars!")
