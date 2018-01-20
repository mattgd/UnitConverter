import unittest
from .context import converter

class TestConvertCircle(unittest.TestCase):

    def test_radians_to_degrees(self):
        self.assertEqual(converter.convert_units(2, "rad", "deg"), "114.59 °")
        self.assertEqual(converter.convert_units(2, "radians", "deg"), "114.59 °")
        self.assertEqual(converter.convert_units(2, "rad", "degrees"), "114.59 °")
        self.assertEqual(converter.convert_units(2, "rad", "degree"), "114.59 °")

    def test_degrees_to_radians(self):
        self.assertEqual(converter.convert_units(114.592, "deg", "rad"), "2.0 rad")
        self.assertEqual(converter.convert_units(114.592, "degree", "rad"), "2.0 rad")
        self.assertEqual(converter.convert_units(114.592, "degrees", "rad"), "2.0 rad")
        self.assertEqual(converter.convert_units(114.592, "deg", "radians"), "2.0 rad")
    

if __name__ == '__main__':
    unittest.main()