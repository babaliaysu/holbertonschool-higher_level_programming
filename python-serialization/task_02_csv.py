#!/usr/bin/env python3
"""CSV faylini JSON formatina ceviren modul."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    CSV faylini oxuyur ve icindekileri data.json faylina yazir.

    Args:
        csv_filename (str): Oxunacaq CSV faylinin adi.

    Returns:
        bool: Ugurlu olarsa True, eks halda False qaytarir.
    """
    try:
        data_list = []
        
        # CSV faylini oxumaq
        with open(csv_filename, mode='r', encoding='utf-8') as csv_f:
            csv_reader = csv.DictReader(csv_f)
            for row in csv_reader:
                data_list.append(row)
        
        # JSON faylina yazmaq
        with open('data.json', mode='w', encoding='utf-8') as json_f:
            json.dump(data_list, json_f, indent=4)
            
        return True
        
    except (FileNotFoundError, Exception):
        return False
