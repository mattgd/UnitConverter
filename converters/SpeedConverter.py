# -*- coding: utf-8 -*-
# Kilometers/hour (kph) and miles/hour (mph)


def kph_to_mph(kph):
    return kph * 0.6214


def mph_to_kph(mph):
    return mph * 1.609


# Kilometers/hour and knots
def kph_to_kt(kph):
    return kph * 0.534


def kt_to_kph(kt):
    return kt * 1.852


# knots and miles/hour
def kt_to_mph(kt):
    return kt_to_kph(kph_to_mph(kt))


def mph_to_kt(mph):
    return mph_to_kph(kph_to_kt(mph))
