# -*- coding: utf-8 -*-
import unittest
from .context import converter

class TestConvertTemperature(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(converter.convert_units(5, "C", "F"), "41.0 °F")
        self.assertEqual(converter.convert_units(5, "Celsius", "F"), "41.0 °F")
        self.assertEqual(converter.convert_units(5, "°c", "F"), "41.0 °F")
        self.assertEqual(converter.convert_units(5, "C", "Fahrenheit"), "41.0 °F")
        self.assertEqual(converter.convert_units(5, "C", "°f"), "41.0 °F")

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(converter.convert_units(41, "F", "C"), "5.0 °C")
        self.assertEqual(converter.convert_units(41, "Fahrenheit", "C"), "5.0 °C")
        self.assertEqual(converter.convert_units(41, "°f", "C"), "5.0 °C")
        self.assertEqual(converter.convert_units(41, "F", "Celsius"), "5.0 °C")
        self.assertEqual(converter.convert_units(41, "F", "°c"), "5.0 °C")

    def test_celsius_to_kelvin(self):
        self.assertEqual(converter.convert_units(5, "C", "K"), "278.15 K")
        self.assertEqual(converter.convert_units(5, "Celsius", "K"), "278.15 K")
        self.assertEqual(converter.convert_units(5, "°c", "K"), "278.15 K")
        self.assertEqual(converter.convert_units(5, "C", "Kelvin"), "278.15 K")

    def test_kelvin_to_celsius(self):
        self.assertEqual(converter.convert_units(278.15, "K", "C"), "5.0 °C")
        self.assertEqual(converter.convert_units(278.15, "Kelvin", "C"), "5.0 °C")
        self.assertEqual(converter.convert_units(278.15, "K", "Celsius"), "5.0 °C")
        self.assertEqual(converter.convert_units(278.15, "K", "°c"), "5.0 °C")
    
    def test_fahrenheit_to_kelvin(self):
        self.assertEqual(converter.convert_units(41, "F", "K"), "278.15 K")
        self.assertEqual(converter.convert_units(41, "Fahrenheit", "K"), "278.15 K")
        self.assertEqual(converter.convert_units(41, "°f", "K"), "278.15 K")
        self.assertEqual(converter.convert_units(41, "F", "Kelvin"), "278.15 K")

    def test_kelvin_to_fahrenheit(self):
        self.assertEqual(converter.convert_units(278.15, "K", "F"), "41.0 °F")
        self.assertEqual(converter.convert_units(278.15, "Kelvin", "F"), "41.0 °F")
        self.assertEqual(converter.convert_units(278.15, "K", "Fahrenheit"), "41.0 °F")
        self.assertEqual(converter.convert_units(278.15, "K", "°f"), "41.0 °F")

    def test_celsius_to_celsius(self):
        print("\n\n", converter.convert_units(5, "C", "C"))
        #self.assertEqual(converter.convert_units(5, "C", "C"), "5.0 °C")
        #self.assertEqual(converter.convert_units(5, "Celsius", "C"), "5.0 °C")
        #self.assertEqual(converter.convert_units(5, "°c", "C"), "5.0 °C")

    def test_fahrenheit_to_fahrenheit(self):
        self.assertEqual(converter.convert_units(41, "F", "F"), "41.0 °F")
        self.assertEqual(converter.convert_units(41, "Fahrenheit", "F"), "41.0 °F")
        self.assertEqual(converter.convert_units(41, "°f", "F"), "41.0 °F")

    def test_kelvin_to_kelvin(self):
        self.assertEqual(converter.convert_units(278.15, "K", "K"), "278.15 K")
        self.assertEqual(converter.convert_units(278.15, "Kelvin", "K"), "278.15 K")
    

if __name__ == '__main__':
    unittest.main()