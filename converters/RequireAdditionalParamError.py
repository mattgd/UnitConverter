# -*- coding: utf-8 -*-
class RequireAdditionalParamError(Exception):
    def __init__(self, additional_params):
        self.additional_params = additional_params
