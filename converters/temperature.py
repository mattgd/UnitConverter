# -*- coding: utf-8 -*-

temperature = {
    "name": "Temperature",
    "units": [
        {
            "name": "Celsius",
            "si": "°C",
            "_internal_accepted_names": [
                "c",
                "celsius",
                "°c",
            ],
            "_internal_function_": "celsius",
            "_internal_conversion": {
                "fahrenheit": lambda celsius: celsius * 1.8 + 32,  # celsius to fahrenheit
                "kelvin": lambda celsius: celsius + 273.15,  # celsius to kelvin
            },
        },
        {
            "name": "Fahrenheit",
            "si": "°F",
            "_internal_accepted_names": [
                "f",
                "fahrenheit",
                "°f",
            ],
            "_internal_function_": "fahrenheit",
            "_internal_conversion": {
                "celsius": lambda fahrenheit: (fahrenheit - 32) / 1.8,  # fahrenheit to celsius
                "kelvin": lambda fahrenheit: (fahrenheit + 459.67) * 5/9,  # fahrenheit to kelvin
            },
        },
        {
            "name": "Kelvin",
            "si": "K",
            "_internal_accepted_names": [
                "k",
                "kelvin",
            ],
            "_internal_function_": "kelvin",
            "_internal_conversion": {
                "celsius": lambda kelvin: kelvin - 273.15,  # kelvin to celsius
                "fahrenheit": lambda kelvin: kelvin * 9/5 - 459.67,  # kelvin to fahrenheit
            },
        },
    ],
}
