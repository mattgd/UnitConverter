# -*- coding: utf-8 -*-
from .CircleConverter import circle_conversions
from .CurrencyConverter import currency_conversions
from .ElectricConverter import electric_conversions
from .ForceConverter import force_conversions
from .PressureConverter import pressure_conversions
from .SpeedConverter import speed_conversions
from .TemperatureConverter import temperature_conversions

UNITS = [
    circle_conversions,
    currency_conversions,
    electric_conversions,
    force_conversions,
    pressure_conversions,
    speed_conversions,
    temperature_conversions,
]
