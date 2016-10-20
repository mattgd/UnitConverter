# -*- coding: utf-8 -*-
from converters.exceptions import ConversionError

electric = {
    "name": "Energy",
    "units": [
        {
            "name": "Watts",
            "si": "W",
            "_internal_accepted_names": [
                "w",
                "watt",
                "watts",
            ],
            "_internal_function_": "watts",
            "_internal_conversion": {
                "volts": lambda watts, amps = None: watts / amps,  # watts to volts
                "ohms": lambda watts, amps = None, volts = None: watts_to_ohms(watts, amps, volts),  # watts to ohms
                "amps": lambda watts, volts = None: watts / volts,  # watts to amps
                "joules": lambda watts, seconds = None: watts * seconds,  # watts to joules
                "horsepower": lambda watts: watts * 746,  # watts to horsepower
                "btups": lambda watts: watts * 0.00095,  # watts to btu
                "cal": lambda watts: watts * 0.23885,  # watts to calories
            },
        },
        {
            "name": "Volts",
            "si": "V",
            "_internal_accepted_names": [
                "v",
                "volt",
                "volts",
            ],
            "_internal_function_": "volts",
        },
        {
            "name": "Ohms",
            "si": "Ω",
            "_internal_accepted_names": [
                "Ω",
                "o",
                "ohm",
                "ohms",
            ],
            "_internal_function_": "ohms",
        },
        {
            "name": "Amps",
            "si": "A",
            "_internal_accepted_names": [
                "a",
                "amp",
                "amps",
                "ampere",
            ],
            "_internal_function_": "amps",
        },
        {
            "name": "Joules",
            "si": "J",
            "_internal_accepted_names": [
                "j",
                "joule",
                "joules",
            ],
            "_internal_function_": "joules",
        },
        {
            "name": "Horsepower",
            "si": "hp",
            "_internal_accepted_names": [
                "hp",
                "horsepower",
            ],
            "_internal_function_": "horsepower",
        },
        {
            "name": "British thermal unit",
            "si": "btu",
            "_internal_accepted_names": [
                "btu",
                "btus",
            ],
            "_internal_function_": "btups",
        },
        {
            "name": "Calories",
            "si": "cal",
            "_internal_accepted_names": [
                "cal",
                "calorie",
                "calories",
            ],
            "_internal_function_": "cal",
        },
    ],
}


# Watts to Ohms given Amps or Volts
def watts_to_ohms(watts, amps = None, volts = None):
    if amps is not None:
        return watts / (amps * amps)
    elif volts is not None:
        return (volts * volts) / watts
    else:
        raise ConversionError("The second given param was not specified correctly. A conversion is not possible.")
