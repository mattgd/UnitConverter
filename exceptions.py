# -*- coding: utf-8 -*-


class ConversionError(Exception):
    """
    Indicates that a conversion is not possible.
    """

    def __init__(self, reason):
        self.reason = reason


class RequireAdditionalParamError(Exception):
    def __init__(self, additional_params):
        self.additional_params = additional_params
