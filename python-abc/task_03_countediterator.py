#!/usr/bin/python3
"""Defines a class CountedIterator that tracks the number of iterations."""


class CountedIterator:
    """An iterator that keeps track of the number of items fetched."""

    def __init__(self, iterable):
        """Initializes the iterator and the counter."""
        self.__iterator = iter(iterable)
        self.__counter = 0

    def get_count(self):
        """Returns the current value of the counter."""
        return self.__counter

    def __next__(self):
        """Increments counter and returns the next item from the iterator."""
        try:
            item = next(self.__iterator)
            self.__counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """Returns the iterator object itself."""
        return self
