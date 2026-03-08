#!/usr/bin/env python3
"""Custom obyektlerin pickle ile serializasiyasi modulu."""
import pickle


class CustomObject:
    """Melumatlari saxlayan ve ozunu serializasiya eden xususi klas."""

    def __init__(self, name, age, is_student):
        """Atributlari teyin edir."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Obyektin atributlarini cap edir."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Obyekti pickle formatinda fayla yazir."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (Exception, OSError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Pickle faylindan obyekti berpa edir."""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (Exception, OSError, pickle.UnpicklingError):
            return None
