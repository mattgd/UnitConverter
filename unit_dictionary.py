# TODO Make this dictionary usable for volume (liters) and mass (grams) as well
class dictionary:

    __metric_dict = {
        'E': 1000000000000000000,
        'P': 1000000000000000,
        'T': 1000000000000,
        'G': 1000000000,
        'M': 1000000,
        'k': 1000,
        'h': 100,
        'da': 10,
        None: 1,
        'd': .1,
        'c': .01,
        'm': .001,
        'μ': .000001,
        'n': .000000001,
        'p': .000000000001,
        'f': .000000000000001,
        'a': .000000000000000001
    }
    __imperial_dist_dict = {
        'lea': 190080,
        'mi': 63360,
        'fu': 7920,
        'ch': 792,
        'rod': 198,
        'yd': 36,
        'ft': 12,
        'li': 7.92,
        'in': 1,
        'th': .001
    }
    __imperial_vol_dict = {
        'gal': 128,
        'qt': 32,
        'pt': 16,
        'gi': 4,
        'floz': 1
    }
    __imperial_mass_dict = {
        't': 2240,
        'cwt': 112,
        'qr': 28,
        'qtr': 28,
        'st': 14,
        'lb': 1,
        'oz': .0625,
        'dr': .00390625,
        'gr': .00014285714
    }

    def metric_dict(self):
        return self.__metric_dict
    def imperial_dist_dict(self):
        return self.__imperial_dist_dict
    def imperial_vol_dict(self):
        return self.__imperial_vol_dict
    def imperial_mass_dict(self):
        return self.__imperial_mass_dict
