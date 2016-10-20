# -*- coding: utf-8 -*-

speed = {
    "name": "Speed",
    "units": [
        {
            "name": "Kilometer per hour",
            "si": "km/h",
            "_internal_accepted_names": [
                "kmh",
                "kph",
            ],
            "_internal_function_": "kph",
            "_internal_conversion": {
                "mph": lambda kph: kph * 0.6214,  # kph to mph
                "kt": lambda kph: kph * 0.534,  # kph to kt
            },
        },
        {
            "name": "Miles per hour",
            "si": "mph",
            "_internal_accepted_names": [
                "mph",
            ],
            "_internal_function_": "mph",
            "_internal_conversion": {
                "kph": lambda mph: mph * 1.609,  # mph to kph
                "kt": lambda mph: mph * 0.868976,  # kph to kt
            },
        },
        {
            "name": "Knots",
            "si": "kn",
            "_internal_accepted_names": [
                "kn",
                "kt",
            ],
            "_internal_function_": "kt",
            "_internal_conversion": {
                "kph": lambda kt: kt * 1.852,  # kt to kph
                "mph": lambda kt: kt * 1.15078,  # kt to mph
            },
        },
    ],
}
