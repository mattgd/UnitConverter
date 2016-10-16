# -*- coding: utf-8 -*-

UNITS = [
    {
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
            },
            {
                "name": "Kelvin",
                "si": "K",
                "_internal_accepted_names": [
                    "k",
                    "kelvin",
                ],
                "_internal_function_": "kelvin",
            },
        ],
    },
    {
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
            },
        ],
    },
    {
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
                "name": "Time",
                "si": "s",
                "_internal_accepted_names": [
                    "s",
                    "sec",
                    "seconds",
                ],
                "_internal_function_": "time",
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
    },
    {
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
            },
            {
                "name": "Bar",
                "si": "bar",
                "_internal_accepted_names": [
                    "bar",
                ],
                "_internal_function_": "bar",
            },
            {
                "name": "Atmosphere",
                "si": "atm",
                "_internal_accepted_names": [
                    "atm",
                    "atmosphere",
                ],
                "_internal_function_": "atm",
            },
            {
                "name": "Torr",
                "si": "torr",
                "_internal_accepted_names": [
                    "torr",
                ],
                "_internal_function_": "torr",
            },
            {
                "name": "Pounds per square inch",
                "si": "psi",
                "_internal_accepted_names": [
                    "psi",
                ],
                "_internal_function_": "psi",
            },
            {
                "name": "Technical atmosphere",
                "si": "at",
                "_internal_accepted_names": [
                    "at",
                ],
                "_internal_function_": "at",
            },
        ],
    },
    {
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
            },
            {
                "name": "Miles per hour",
                "si": "mph",
                "_internal_accepted_names": [
                    "mph",
                ],
                "_internal_function_": "mph",
            },
            {
                "name": "Knots",
                "si": "kn",
                "_internal_accepted_names": [
                    "kn",
                    "kt",
                ],
                "_internal_function_": "kt",
            },
        ],
    },
    {
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
            },
        ],
    },
    {
        "name": "Currency",
        "units": [
            {
                "name": "Australian dollars",
                "si": "AUD",
                "_internal_accepted_names": [
                    "aud",
                    "australian dollar",
                    "australian dollars",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Bulgarian lev",
                "si": "BGN",
                "_internal_accepted_names": [
                    "bgn",
                    "bulgarian lev",
                    "lev",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Brazil reais",
                "si": "BRL",
                "_internal_accepted_names": [
                    "brl",
                    "brazil reais",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Canadian dollar",
                "si": "CAD",
                "_internal_accepted_names": [
                    "cad",
                    "canadian dollar",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Swiss francs",
                "si": "CHF",
                "_internal_accepted_names": [
                    "chf",
                    "franc",
                    "francs",
                    "swiss franc",
                    "swiss francs",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Chinese yuan",
                "si": "CNY",
                "_internal_accepted_names": [
                    "cny",
                    "yuan",
                    "chinese yuan",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Czech koruny",
                "si": "CZK",
                "_internal_accepted_names": [
                    "czk",
                    "czech koruny",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Danish kroner",
                "si": "DKK",
                "_internal_accepted_names": [
                    "dkk",
                    "danish kroner",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "British pounds",
                "si": "GBP",
                "_internal_accepted_names": [
                    "gbp",
                    "pounds",
                    "british pounds",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Euros",
                "si": "EUR",
                "_internal_accepted_names": [
                    "eur",
                    "euro",
                    "euros",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Hong Kong dollars",
                "si": "HKD",
                "_internal_accepted_names": [
                    "hkd",
                    "hong kong dollar",
                    "hong kong dollars",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Croatian kune",
                "si": "HRK",
                "_internal_accepted_names": [
                    "hrk",
                    "croatian kune",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Hungarian Forint",
                "si": "HUF",
                "_internal_accepted_names": [
                    "huf",
                    "hungarian forint",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Indonesian Rupiah",
                "si": "IDR",
                "_internal_accepted_names": [
                    "idr",
                    "rupiah",
                    "indonesian rupiah",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Israeli Shekel",
                "si": "ILS",
                "_internal_accepted_names": [
                    "ils",
                    "shekel",
                    "israeli shekel",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Indian rupees",
                "si": "INR",
                "_internal_accepted_names": [
                    "inr",
                    "rupees",
                    "indian rupees",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Japanese yen",
                "si": "JPY",
                "_internal_accepted_names": [
                    "jpy",
                    "yen",
                    "japanese yen",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "South Korean won",
                "si": "KRW",
                "_internal_accepted_names": [
                    "krw",
                    "won",
                    "south korean won",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Mexican pesos",
                "si": "MXN",
                "_internal_accepted_names": [
                    "mxn",
                    "pesos",
                    "mexican pesos",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Malaysian Ringgit",
                "si": "MYR",
                "_internal_accepted_names": [
                    "myr",
                    "ringgit",
                    "malaysian ringgit",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Norwegian krone",
                "si": "NOK",
                "_internal_accepted_names": [
                    "nok",
                    "norwegian krone",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "New Zealand dollars",
                "si": "NZD",
                "_internal_accepted_names": [
                    "nzd",
                    "new zealand dollars",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Philippines peso",
                "si": "PHP",
                "_internal_accepted_names": [
                    "php",
                    "philippines peso",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Polish zloty",
                "si": "PLN",
                "_internal_accepted_names": [
                    "pln",
                    "zloty",
                    "polish zloty",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Romanian Leu",
                "si": "RON",
                "_internal_accepted_names": [
                    "ron",
                    "leu",
                    "romanian leu",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Russian ruble",
                "si": "RUB",
                "_internal_accepted_names": [
                    "rub",
                    "ruble",
                    "russian ruble",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Swedish kronor",
                "si": "SEK",
                "_internal_accepted_names": [
                    "sek",
                    "kronor",
                    "swedish kronor",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Singapore dollars",
                "si": "SGD",
                "_internal_accepted_names": [
                    "sgd",
                    "singapore dollar",
                    "singapore dollars",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Thai baht",
                "si": "THB",
                "_internal_accepted_names": [
                    "thb",
                    "baht",
                    "thai baht",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "Turkish Lira",
                "si": "TRY",
                "_internal_accepted_names": [
                    "try",
                    "lira",
                    "turkish lira",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "US Dollar",
                "si": "USD",
                "_internal_accepted_names": [
                    "usd",
                    "dollar",
                    "dollars",
                    "us dollar",
                    "us dollars",
                ],
                "_internal_function_": "cur",
            },
            {
                "name": "South African rands",
                "si": "ZAR",
                "_internal_accepted_names": [
                    "zar",
                    "rands",
                    "south african rands",
                ],
                "_internal_function_": "cur",
            },
        ],
    },
]
