# -*- coding: utf-8 -*-
import unittest
from .context import converter

class TestConvertCurrency(unittest.TestCase):

    def test_newtons_to_dynes(self):
        self.assertEqual(converter.convert_units(1, "n", "dyn"), "100000.0 dyn")
        self.assertEqual(converter.convert_units(1, "newton", "dyn"), "100000.0 dyn")
        self.assertEqual(converter.convert_units(1, "newtons", "dyn"), "100000.0 dyn")
        self.assertEqual(converter.convert_units(1, "n", "dyne"), "100000.0 dyn")
        self.assertEqual(converter.convert_units(1, "n", "dynes"), "100000.0 dyn")
    
    def test_newtons_to_poundals(self):
        self.assertEqual(converter.convert_units(1, "n", "pdl"), "7.23 pdl")
        self.assertEqual(converter.convert_units(1, "newton", "pdl"), "7.23 pdl")
        self.assertEqual(converter.convert_units(1, "newtons", "pdl"), "7.23 pdl")
        self.assertEqual(converter.convert_units(1, "n", "poundal"), "7.23 pdl")
        self.assertEqual(converter.convert_units(1, "n", "poundals"), "7.23 pdl")

    def test_newtons_to_kilogram_force(self):
        self.assertEqual(converter.convert_units(100, "n", "kp"), "10.2 kp")
        self.assertEqual(converter.convert_units(100, "newton", "kp"), "10.2 kp")
        self.assertEqual(converter.convert_units(100, "newtons", "kp"), "10.2 kp")
        self.assertEqual(converter.convert_units(100, "n", "kgf"), "10.2 kp")
        self.assertEqual(converter.convert_units(100, "n", "kps"), "10.2 kp")

    def test_dyne_to_newtons(self):
        self.assertEqual(converter.convert_units(100000, "dyn", "n"), "1.0 N")
        self.assertEqual(converter.convert_units(100000.0, "dyne", "n"), "1.0 N")
        self.assertEqual(converter.convert_units(100000.0, "dynes", "n"), "1.0 N")
        self.assertEqual(converter.convert_units(100000.0, "dyn", "newton"), "1.0 N")
        self.assertEqual(converter.convert_units(100000.0, "dyn", "newtons"), "1.0 N")
    
    def test_dyne_to_poundals(self):
        self.assertEqual(converter.convert_units(100000, "dyn", "pdl"), "7.23 pdl")
        self.assertEqual(converter.convert_units(100000, "dyne", "pdl"), "7.23 pdl")
        self.assertEqual(converter.convert_units(100000, "dynes", "pdl"), "7.23 pdl")
        self.assertEqual(converter.convert_units(100000, "dyn", "poundal"), "7.23 pdl")
        self.assertEqual(converter.convert_units(100000, "dyn", "poundals"), "7.23 pdl")

    def test_dyne_to_kilogram_force(self):
        self.assertEqual(converter.convert_units(10000000, "dyn", "kp"), "10.2 kp")
        self.assertEqual(converter.convert_units(10000000, "dyne", "kp"), "10.2 kp")
        self.assertEqual(converter.convert_units(10000000, "dynes", "kp"), "10.2 kp")
        self.assertEqual(converter.convert_units(10000000, "dyn", "kgf"), "10.2 kp")
        self.assertEqual(converter.convert_units(10000000, "dyn", "kps"), "10.2 kp")

    def test_poundal_to_newtons(self):
        self.assertEqual(converter.convert_units(100, "pdl", "n"), "13.83 N")
        self.assertEqual(converter.convert_units(100, "poundal", "n"), "13.83 N")
        self.assertEqual(converter.convert_units(100, "poundals", "n"), "13.83 N")
        self.assertEqual(converter.convert_units(100, "pdl", "newton"), "13.83 N")
        self.assertEqual(converter.convert_units(100, "pdl", "newtons"), "13.83 N")
    
    def test_poundal_to_dynes(self):
        self.assertEqual(converter.convert_units(1, "pdl", "dyn"), "13825.5 dyn")
        self.assertEqual(converter.convert_units(1, "poundal", "dyn"), "13825.5 dyn")
        self.assertEqual(converter.convert_units(1, "poundals", "dyn"), "13825.5 dyn")
        self.assertEqual(converter.convert_units(1, "pdl", "dyne"), "13825.5 dyn")
        self.assertEqual(converter.convert_units(1, "pdl", "dynes"), "13825.5 dyn")

    def test_poundal_to_kilogram_force(self):
        self.assertEqual(converter.convert_units(100, "pdl", "kp"), "1.41 kp")
        self.assertEqual(converter.convert_units(100, "poundal", "kp"), "1.41 kp")
        self.assertEqual(converter.convert_units(100, "poundals", "kp"), "1.41 kp")
        self.assertEqual(converter.convert_units(100, "pdl", "kgf"), "1.41 kp")
        self.assertEqual(converter.convert_units(100, "pdl", "kps"), "1.41 kp")

    def test_kilogram_force_to_newtons(self):
        self.assertEqual(converter.convert_units(1, "kp", "n"), "9.81 N")
        self.assertEqual(converter.convert_units(1, "kgf", "n"), "9.81 N")
        self.assertEqual(converter.convert_units(1, "kps", "n"), "9.81 N")
        self.assertEqual(converter.convert_units(1, "kp", "newton"), "9.81 N")
        self.assertEqual(converter.convert_units(1, "kp", "newtons"), "9.81 N")
    
    def test_kilogram_force_to_dynes(self):
        self.assertEqual(converter.convert_units(1, "kp", "dyn"), "980665.0 dyn")
        self.assertEqual(converter.convert_units(1, "kgf", "dyn"), "980665.0 dyn")
        self.assertEqual(converter.convert_units(1, "kps", "dyn"), "980665.0 dyn")
        self.assertEqual(converter.convert_units(1, "kp", "dyne"), "980665.0 dyn")
        self.assertEqual(converter.convert_units(1, "kp", "dynes"), "980665.0 dyn")

    def test_kilogram_force_to_poundals(self):
        self.assertEqual(converter.convert_units(1, "kp", "pdl"), "70.93 pdl")
        self.assertEqual(converter.convert_units(1, "kgf", "pdl"), "70.93 pdl")
        self.assertEqual(converter.convert_units(1, "kps", "pdl"), "70.93 pdl")
        self.assertEqual(converter.convert_units(1, "kp", "poundal"), "70.93 pdl")
        self.assertEqual(converter.convert_units(1, "kp", "poundals"), "70.93 pdl")
    

if __name__ == '__main__':
    unittest.main()