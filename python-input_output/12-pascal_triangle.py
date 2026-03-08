#!/usr/bin/python3
"""Paskal ucbucagi yaradan modul."""


def pascal_triangle(n):
    """
    n olculu Paskal ucbucagini siyahilar siyahisi kimi qaytarir.
    
    Args:
        n (int): Ucducagin setir sayi.
        
    Returns:
        list: Tam ededlerden ibaret siyahilar siyahisi.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Ilk setir hemise [1] olur

    for i in range(1, n):
        prev_row = triangle[i - 1]
        # Her yeni setir hemise 1 ile baslayir
        current_row = [1]

        # Ortadaki ededleri hesablamaq: yuxari setirdeki qonsu ededlerin cemi
        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        # Her yeni setir hemise 1 ile bitir
        current_row.append(1)
        triangle.append(current_row)

    return triangle
