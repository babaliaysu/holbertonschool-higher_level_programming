#!/usr/bin/env python3
"""XML formatinda serializasiya ucun modul."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Lugeti XML formatina cevirir ve fayla yazir.

    Args:
        dictionary (dict): Serializasiya edilecek melumat.
        filename (str): Saxlanilacaq faylin adi.
    """
    # Kok elementi yaradirir: <data>
    root = ET.Element("data")

    # Lugetdeki her bir acari teq, deyeri ise teqin metni kimi elave edirik
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Element agacini (tree) yaradib fayla yaziriq
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    XML faylini oxuyub lugete cevirir.

    Args:
        filename (str): Oxunacaq XML faylinin adi.

    Returns:
        dict: Berpa edilmis luget.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        # Kokun altindaki elementlerden luget qururuq
        return {child.tag: child.text for child in root}
    except (FileNotFoundError, ET.ParseError):
        return None
