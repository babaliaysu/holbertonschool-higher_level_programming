#!/usr/bin/python3
"""max_integer funksiyasi ucun Unittest"""

import unittest
# Funksiyani esas fayldan bura cagiririq
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """max_integer funksiyasini yoxlayan testler"""

    def test_ordered_list(self):
        """Artan sira ile olan siyahini yoxla"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Qarisiq sira ile olan siyahini yoxla"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Bos siyahini yoxla (None qaytarmalidir)"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Tek elementi olan siyahini yoxla"""
        self.assertEqual(max_integer([10]), 10)

    def test_max_at_beginning(self):
        """En boyuk reqem basda olanda yoxla"""
        self.assertEqual(max_integer([100, 50, 10]), 100)

    def test_negatives(self):
        """Siyahida menfi reqemler olanda yoxla"""
        self.assertEqual(max_integer([-1, -5, -2]), -1)

    def test_floats(self):
        """Siyahida onluq kesrler olanda yoxla"""
        self.assertEqual(max_integer([1.5, 2.7, 0.5]), 2.7)

if __name__ == '__main__':
    unittest.main()
