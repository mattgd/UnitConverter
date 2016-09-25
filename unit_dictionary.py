metric_dist_dict = {
    'Em': 1000000000000000000,
    'Pm': 1000000000000000,
    'Tm': 1000000000000,
    'Gm': 1000000000,
    'Mm': 1000000,
    'km': 1000,
    'hm': 100,
    'dam': 10,
    'm': 1,
    'dm': .1,
    'cm': .01,
    'mm': .001,
    'μm': .000001,
    'nm': .000000001,
    'pm': .000000000001,
    'fm': .000000000000001,
    'am': .000000000000000001
}
imperial_dist_dict = {
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

def metric_dict():
    return metric_dist_dict
def imperial_dict():
    return imperial_dist_dict
