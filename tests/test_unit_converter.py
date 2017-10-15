import unittest
from .context import converter

class TestConvertTemperature(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(converter.convert_units(5, "C", "F"), "41.0 °F")

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(converter.convert_units(41, "F", "C"), "5.0 °C")

    def test_celsius_to_kelvin(self):
        self.assertEqual(converter.convert_units(5, "C", "K"), "278.15 K")

    def test_kelvin_to_celsius(self):
        self.assertEqual(converter.convert_units(278.15, "K", "C"), "5.0 °C")
    
    def test_fahrenheit_to_kelvin(self):
        self.assertEqual(converter.convert_units(41, "F", "K"), "278.15 K")

    def test_kelvin_to_fahrenheit(self):
        self.assertEqual(converter.convert_units(278.15, "K", "F"), "41.0 °F")

    def test_celsius_to_celsius(self):
        self.assertEqual(converter.convert_units(5, "C", "C"), "5 °C")

    def test_fahrenheit_to_fahrenheit(self):
        self.assertEqual(converter.convert_units(41, "F", "F"), "41 °F")

    def test_kelvin_to_kelvin(self):
        self.assertEqual(converter.convert_units(278.15, "K", "K"), "278.15 K")
    

if __name__ == '__main__':
    unittest.main()