#!/usr/bin/python3

def write_file(filename="", text=""):
    """Fayla metn yazir ve yazilan simvollarin sayini qaytarir."""
    with open(filename, "w", encoding="utf-8") as new_file:
        return new_file.write(text)
