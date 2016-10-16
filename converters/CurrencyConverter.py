# -*- coding: utf-8 -*-
import requests
import json
from ConversionError import ConversionError


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
    session.trust_env = False # disable proxy settings

    response = session.get(_build_convert_url(from_unit, to_unit))
    if response.ok:
        result = json.loads(response.content)
        return money * float(result["rates"][to_unit])
    raise ConversionError("Could not load current exchange rates from server")


def _build_convert_url(from_unit, to_unit):
    return "https://api.fixer.io/latest?base=" + from_unit + "&symbols=" + to_unit
