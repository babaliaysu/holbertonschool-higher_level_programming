#!/usr/bin/python3
"""Defines classes for Fish, Bird, and a hybrid FlyingFish."""


class Fish:
    """Represents a fish with swimming abilities."""

    def swim(self):
        """Prints the swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Represents a bird with flying abilities."""

    def fly(self):
        """Prints the flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Prints the habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish, inheriting from both Fish and Bird."""

    def fly(self):
        """Overrides the fly method for a flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides the swim method for a flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides the habitat method for a flying fish."""
        print("The flying fish lives both in water and the sky!")
