#!/usr/bin/python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that should return the sound of the animal."""
        pass


class Dog(Animal):
    """Subclass representing a dog."""

    def sound(self):
        """Returns the bark sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Subclass representing a cat."""

    def sound(self):
        """Returns the meow sound of a cat."""
        return "Meow"
