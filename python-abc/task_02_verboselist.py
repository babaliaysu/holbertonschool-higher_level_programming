#!/usr/bin/python3
"""Defines a class VerboseList that extends the built-in list class."""


class VerboseList(list):
    """A list that prints notifications when modified."""

    def append(self, item):
        """Adds an item and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extends the list and prints the number of items added."""
        item_count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(item_count))

    def remove(self, item):
        """Prints notification before removing an item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Prints notification before popping an item."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
