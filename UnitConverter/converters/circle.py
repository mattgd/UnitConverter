# -*- coding: utf-8 -*-

import math


circle = {
    "name": "Circle",
    "units": [
        {
            "name": "Radians",
            "si": "rad",
            "_internal_accepted_names": [
                "rad",
                "radians",
            ],
            "_internal_function_": "radians",
            "_internal_conversion": {
                "degrees": lambda radians: math.degrees(radians),  # radians to degrees
            }
        },
        {
            "name": "Degrees",
            "si": "°",
            "_internal_accepted_names": [
                "deg",
                "degree",
                "degrees",
            ],
            "_internal_function_": "degrees",
            "_internal_conversion": {
                "radians": lambda degrees: math.radians(degrees),  # degrees to radians
            }
        },
    ],
}
