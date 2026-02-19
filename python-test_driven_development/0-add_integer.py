#!/usr/bin/python3
"""
Bu modul iki ədədi toplayan add_integer funksiyasını ehtiva edir.
"""


def add_integer(a, b=98):
    """
    İki tam ədədi toplayır.
    
    Arqumentlər:
        a: Birinci ədəd (int və ya float)
        b: İkinci ədəd (int və ya float, default olaraq 98)
        
    Returns:
        İki ədədin cəmi (int)
        
    Raises:
        TypeError: Əgər a və ya b int/float deyilsə
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
