#!/usr/bin/python3
"""Student klasini diskde saxlamaq ve yuklemek ucun modul."""


class Student:
    """Telebe melumatlarini saxlayan ve idare eden klas."""

    def __init__(self, first_name, last_name, age):
        """Telebe obyektini yaradir."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Obyektin dictionary temsilini qaytarir."""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            # Yalniz attrs siyahisinda olan atributlari secirik
            res = {}
            for a in attrs:
                if hasattr(self, a):
                    res[a] = getattr(self, a)
            return res
        # Eger attrs yoxdursa, butun atributlari qaytaririq
        return self.__dict__

    def reload_from_json(self, json):
        """Dictionary-deki melumatlarla obyekti yenileyir."""
        for key, value in json.items():
            setattr(self, key, value)
