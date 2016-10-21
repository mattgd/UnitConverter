# -*- coding: utf-8 -*-
from units import UNITS
from converters.exceptions import ConversionError, RequireAdditionalParamError


def convert(from_unit, to_unit, *args, **kwargs):
    """
    Convert the value from one unit to another
    :param from_unit: Source unit
    :param to_unit: Target unit
    :param args: Additional parameters (values)
    :param kwargs: Additional parameters (additional values like for conversion watts to ohms)
    :return: Converted number
    """
    if not can_convert(from_unit, to_unit):
        raise ConversionError("Cannot convert from {0} to {1}".format(from_unit, to_unit))

    try:
        category = _find_unit_category(from_unit)

        # handle special method (currently for currency conversion)
        if "general_method" in category:
            # currency function does take the from_unit and to_unit as param
            additional_params = {"from_unit": from_unit, "to_unit": to_unit}
            return category["general_method"](*args, **additional_params)

        convert_function = _find_unit(from_unit)["_internal_conversion"][_find_unit(to_unit)["_internal_function_"]]
        missing_si_varname = map(lambda varname: get_si(varname), convert_function.func_code.co_varnames)

        if len(args) + len(kwargs) < len(missing_si_varname):
            for i in range(len(args) + len(kwargs)):
                # remove already given variables
                missing_si_varname.pop(0)
                # only not given variable names are listed
            if convert_function.func_defaults is not None and len(convert_function.func_defaults) == len(
                    missing_si_varname):
                # should not be >= because if all other params are optional
                # it means that only one has to be set for the function to work (specification)
                raise RequireAdditionalParamError(missing_si_varname)

        # take the named additional params and map the si to the "_internal_function_" name
        additional_params = {_find_unit(k)['_internal_function_']: v for k, v in kwargs.iteritems()}

        return convert_function(*args, **additional_params)
    except AttributeError:
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


def get_suggestions_for_category(category = None):
    """
    Returns categories currently accepted by the program.
    :param category: Optional. If given: search all units for the given category.
                        If not given give all categories.
    :return:    Returns all categories accepted if no category was given.
                If a category was given returns all units for that category.
    """
    if category is not None:
        # a category was given -> all units for that category
        category = _find_category(category)

        if category is None:
            return None

        return [_format_unit_output(unit)
                for unit in category["units"]]

    # no category was given -> give all possible categories
    return [category["name"]
            for category in UNITS]


def get_suggestions_to_given_unit(unit):
    """
    Lists all units that the given unit can be converted to
    :param unit: The unit which should be converted
    :return: All units that the given unit can be converted to
    """
    unit = _find_unit(unit)

    if unit is None:
        return None

    return [_format_unit_output(single_unit)
            for single_unit in _find_unit_category(unit["_internal_function_"])["units"]
            if unit["si"] not in single_unit["_internal_accepted_names"]                    # the given unit should not be listed as a "convert to" unit
            and "_internal_conversion" in single_unit                                       # catch lazy programmers faults (no _internal_conversion to one unit)
            and unit["_internal_function_"] in single_unit["_internal_conversion"]]         # the given unit should be convertable to the single_unit


def _find_category(category_name):
    """
    Internal: Load a category by name from the UNITS array
    :param category_name: The category name to search the array to
    :return: The category from the UNITS array or None if none was found
    """
    for category in UNITS:
        if category_name.lower() == category["name"].lower():
            return category
    return None


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
            if unit in cat_unit["_internal_accepted_names"] or unit == cat_unit["name"].lower():
                return cat_unit
    return None


def _format_unit_output(unit):
    """
    Formats an unit to get outputed by the system (Format: "<name> (<function_name to enter>)")
    :param unit:
    :return:
    """
    return unit["name"] + " (" + unit["_internal_function_"] + ")"
