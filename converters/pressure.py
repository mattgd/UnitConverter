# -*- coding: utf-8 -*-

pressure = {
    "name": "Pressure",
    "units": [
        {
            "name": "Pascal",
            "si": "Pa",
            "_internal_accepted_names": [
                "pa",
                "pascal",
            ],
            "_internal_function_": "pa",
            "_internal_conversion": {
                "bar": lambda pascal: pascal * 0.00001,  # pascal to bar
                "atm": lambda pascal: pascal / 101325,  # pascal to atmosphere
                "torr": lambda pascal: pascal * 0.00750062,  # pascal to torr
                "psi": lambda pascal: pascal / 6894.76,  # pascal to psi
                "at": lambda pascal: pascal * 1.01971621298E-5,  # pascal to at
            },
        },
        {
            "name": "Bar",
            "si": "bar",
            "_internal_accepted_names": [
                "bar",
            ],
            "_internal_function_": "bar",
            "_internal_conversion": {
                "pascal": lambda bar: bar / 0.00001,  # bar to pascal
                "atm": lambda bar: bar / 1.01325,  # bar to atmosphere
                "torr": lambda bar: bar * 750.062,  # bar to torr
                "psi": lambda bar: bar * 750.062,  # bar to psi
                "at": lambda bar: bar * 1.01972,  # bar to at
            },
        },
        {
            "name": "Atmosphere",
            "si": "atm",
            "_internal_accepted_names": [
                "atm",
                "atmosphere",
            ],
            "_internal_function_": "atm",
            "_internal_conversion": {
                "pascal": lambda atm: atm * 101325,  # atm to pascal
                "bar": lambda atm: atm * 1.01325,  # atm to bar
                "torr": lambda atm: atm * 760,  # atm to torr
                "psi": lambda atm: atm * 14.6959,  # atm to psi
                "at": lambda atm: atm * 1.03322755477,  # atm to at
            },
        },
        {
            "name": "Torr",
            "si": "torr",
            "_internal_accepted_names": [
                "torr",
            ],
            "_internal_function_": "torr",
            "_internal_conversion": {
                "pascal": lambda torr: torr / 0.00750062,  # torr to pascal
                "bar": lambda torr: torr / 750.062,  # torr to bar
                "atm": lambda torr: torr / 760,  # torr to atm
                "psi": lambda torr: torr / 51.7149,  # torr to psi
                "at": lambda torr: torr * 0.00135950982242,  # torr to at
            },
        },
        {
            "name": "Pounds per square inch",
            "si": "psi",
            "_internal_accepted_names": [
                "psi",
            ],
            "_internal_function_": "psi",
            "_internal_conversion": {
                "pascal": lambda psi: psi * 6894.76,  # psi to pascal
                "bar": lambda psi: psi / 14.5038,  # psi to bar
                "atm": lambda psi: psi / 14.6959,  # psi to atm
                "torr": lambda psi: psi * 51.7149,  # psi to torr
                "at": lambda psi: psi * 0.0703069578296,  # psi to at
            },
        },
        {
            "name": "Technical atmosphere",
            "si": "at",
            "_internal_accepted_names": [
                "at",
            ],
            "_internal_function_": "at",
            "_internal_conversion": {
                "pascal": lambda at: at / 1.01971621298E-5,  # at to pascal
                "bar": lambda at: at / 1.0197,  # at to bar
                "atm": lambda at: at / 1.03322755477,  # at to atm
                "torr": lambda at: at / 0.00135950982242,  # at to torr
                "psi": lambda at: at / 0.0703069578296,  # at to at
            },
        },
    ],
}
