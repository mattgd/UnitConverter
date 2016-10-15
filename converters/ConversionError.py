# -*- coding: utf-8 -*-
class ConversionError(Exception):
    """
    Indicates that a conversion is not possible.
    """

    def __init__(self, reason):
        self.reason = reason
