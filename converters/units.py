# -*- coding: utf-8 -*-
from .circle import circle_conversions
from .currency import currency_conversions
from .electric import electric_conversions
from .force import force_conversions
from .pressure import pressure_conversions
from .speed import speed_conversions
from .temperature import temperature_conversions

UNITS = [
    circle_conversions,
    currency_conversions,
    electric_conversions,
    force_conversions,
    pressure_conversions,
    speed_conversions,
    temperature_conversions,
]
