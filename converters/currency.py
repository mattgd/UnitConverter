# -*- coding: utf-8 -*-
import requests
import json
from converters.exceptions import ConversionError

currency = {
    "name": "Currency",
    "general_method": lambda money, from_unit, to_unit: cur_to_cur(money, from_unit, to_unit),
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
}


# this is the only needed converter function (requesting http://fixer.io/)
# the currencies to convert from and to are given as params
def cur_to_cur(money, from_unit, to_unit):
    """
    Converts money from from_unit to to_unit
    :param money: The given amount of money to convert
    :param from_unit: The currency to convert from
    :param to_unit: The currency to convert to
    :return: Converted money in to_unit
    """
    session = requests.Session()
    session.trust_env = False  # disable proxy settings

    response = session.get(_build_convert_url(from_unit, to_unit))
    if response.ok:
        result = json.loads(response.content)
        return money * float(result["rates"][to_unit])
    raise ConversionError("Could not load current exchange rates from server")


def _build_convert_url(from_unit, to_unit):
    return "https://api.fixer.io/latest?base=" + from_unit + "&symbols=" + to_unit
