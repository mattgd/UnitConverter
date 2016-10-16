# -*- coding: utf-8 -*-
from Converter import UNITS
from ConversionError import ConversionError
from RequireAdditionalParamError import RequireAdditionalParamError

# import all converters (all methods) to call them here
from TemperatureConverter import *
from CircleConverter import *
from ElectricConverter import *
from PressureConverter import *
from SpeedConverter import *
from ForceConverter import *
from CurrencyConverter import *

possibles = globals().copy()
possibles.update(locals())


def convert(from_unit, to_unit, *args, **kwargs):
    """
    Convert the value from one unit to another
    :param from_unit: Source unit
    :param to_unit: Target unit
    :param args: Additional parameters (values)
    :return: Converted number
    """
    if not can_convert(from_unit, to_unit):
        raise ConversionError("Cannot convert from {0} to {1}".format(from_unit, to_unit))

    try:
        convert_function = _build_method(from_unit, to_unit)

        missing_si_varname = map(lambda varname: get_si(varname), convert_function.func_code.co_varnames)

        if len(args) + len(kwargs) < len(missing_si_varname):
            for i in range(len(args) + len(kwargs)):
                # remove already given variables
                missing_si_varname.pop(0)
            # only not given variable names are listed
            if convert_function.func_defaults is not None and len(convert_function.func_defaults) == len(missing_si_varname):
                # should not be >= because if all other params are optional
                # it means that only one has to be set for the function to work (specification)
                raise RequireAdditionalParamError(missing_si_varname)

        # take the named additional params and map the si to the "_internal_function_" name
        additional_params = {_find_unit(k)['_internal_function_']: v for k, v in kwargs.iteritems()}

        if (_find_unit_category(from_unit)["name"] == "Currency"):
            # currency function does take the from_unit and to_unit as param
            additional_params["from_unit"] = from_unit
            additional_params["to_unit"] = to_unit

        return convert_function(*args, **additional_params)
    except AttributeError as e:
        raise ConversionError("No conversion possible")


def can_convert(from_unit, to_unit):
    """
    Check if the given units can be converted
    :param from_unit: The source unit to convert from
    :param to_unit: The target unit to convert to
    :return: bool - true if unit can be converted
                    false otherwise
    """
    # There must be an implementation to convert the units
    from_unit_category = _find_unit_category(from_unit)
    to_unit_category = _find_unit_category(to_unit)

    if from_unit_category is None or to_unit_category is None:
        return False

    # The units have to be in the same category (mph to watts does not make any sense)
    if from_unit_category["name"] != to_unit_category["name"]:
        return False

    return True


def get_si(unit):
    """
    Load the SI string for the given unit
    :param unit: The unit for which the SI string should be loaded
    :return: String - SI string or None if none was found
    """
    cat_unit = _find_unit(unit)
    if cat_unit is None:
        return None
    return cat_unit["si"]


def _find_unit_category(unit):
    """
    Internal: Load the category of one unit from the UNITS array
    :param unit: The unit which should be included in the '_internal_accepted_names' in a category of the UNITS array
    :return: The category from the UNITS array or None if none was found
    """
    unit = unit.lower()
    for category in UNITS:
        for cat_unit in category["units"]:
            if unit in cat_unit["_internal_accepted_names"]:
                return category
    return None


def _find_unit(unit):
    """
    Internal: Load one specific unit from the UNITS array
    :param unit: The name of the unit (should be included in the '_internal_accepted_names' or 'name')
    :return: The unit from the UNITS array or None if none was found
    """
    unit = unit.lower()
    for category in UNITS:
        for cat_unit in category["units"]:
            if unit in cat_unit["_internal_accepted_names"] or unit == cat_unit["name"]:
                return cat_unit
    return None


def _build_method(from_unit, to_unit):
    """
    Internal: Build the method call to convert
    :param from_unit: The source unit to convert from
    :param to_unit: The target unit to convert to
    :return: A method call function
    """
    from_unit = _find_unit(from_unit)
    to_unit = _find_unit(to_unit)

    return possibles.get(from_unit["_internal_function_"] + "_to_" + to_unit["_internal_function_"])
