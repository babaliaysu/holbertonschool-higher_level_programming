#!/usr/bin/env python3
"""JSON formatinda serializasiya ucun modul."""
import json


def serialize_and_save_to_file(data, filename):
    """Lugeti JSON faylina yazir."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """JSON faylini oxuyub lugete cevirir."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
