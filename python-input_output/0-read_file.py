#!/usr/bin/python3
"""Faylı oxumaq üçün modul."""


def read_file(filename=""):
    """Faylı UTF8 formatında oxuyur və stdout-a çap edir."""
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
