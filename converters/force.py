# -*- coding: utf-8 -*-

force = {
    "name": "Force",
    "units": [
        {
            "name": "Newtons",
            "si": "N",
            "_internal_accepted_names": [
                "n",
                "newton",
                "newtons",
            ],
            "_internal_function_": "n",
            "_internal_conversion": {
                "dyn": lambda n: n * 10 ** 5,  # n to dyn
                "pdl": lambda n: n * 7.23301,  # n to pdl
                "kp": lambda n: n * 0.10197,  # n to kp
            },
        },
        {
            "name": "Dyne",
            "si": "dyn",
            "_internal_accepted_names": [
                "dyn",
                "dyne",
                "dynes",
            ],
            "_internal_function_": "dyn",
            "_internal_conversion": {
                "n": lambda dyn: dyn * 0.00001,  # dyn to n
                "pdl": lambda dyn: dyn / 13825.4954376,  # dyn to pdl
                "kp": lambda dyn: dyn * 1.01972E-6,  # dyn to kp
            },
        },
        {
            "name": "Poundals",
            "si": "pdl",
            "_internal_accepted_names": [
                "pdl",
                "poundal",
                "poundals",
            ],
            "_internal_function_": "pdl",
            "_internal_conversion": {
                "n": lambda pdl: pdl * 0.1382549544,  # pdl to n
                "dyn": lambda pdl: pdl * 13825.4954376,  # pdl to dyn
                "kp": lambda pdl: pdl * 0.01409808185017,  # pdl to kp
            },
        },
        {
            "name": "Kilogram-force",
            "si": "kp",
            "_internal_accepted_names": [
                "kp",
                "kgf",
                "kps",
            ],
            "_internal_function_": "kp",
            "_internal_conversion": {
                "n": lambda kp: kp * 9.80665,  # kp to n
                "dyn": lambda kp: kp * 980665,  # kp to dyn
                "pdl": lambda kp: kp * 70.93163528397,  # kp to pdl
            },
        },
    ],
}
