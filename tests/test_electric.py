# -*- coding: utf-8 -*-
import unittest
from .context import converter

class TestConvertCurrency(unittest.TestCase):

    def test_watts_to_horsepower(self):
        self.assertEqual(converter.convert_units(745.7, "w", "hp"), "1.0 hp")
        self.assertEqual(converter.convert_units(745.7, "watt", "hp"), "1.0 hp")
        self.assertEqual(converter.convert_units(745.7, "watts", "hp"), "1.0 hp")
        self.assertEqual(converter.convert_units(745.7, "w", "horsepower"), "1.0 hp")
    
    def test_horsepower_to_watts(self):
        self.assertEqual(converter.convert_units(1, "hp", "w"), "745.7 W")
        self.assertEqual(converter.convert_units(1, "horsepower", "w"), "745.7 W")
        self.assertEqual(converter.convert_units(1, "hp", "watt"), "745.7 W")
        self.assertEqual(converter.convert_units(1, "hp", "watts"), "745.7 W")
    

if __name__ == '__main__':
    unittest.main()