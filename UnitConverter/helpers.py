from . import unit_dictionary
from .converters import convert, can_convert, get_si
from .converters.exceptions import ConversionError, RequireAdditionalParamError


# TIME CONVERSION
def convert_time(value, units_from_base, units_to_base):
    return value * units_from_base / units_to_base


def check_time(value, units_from, units_to, decimal_places):
    dictionary = unit_dictionary.Dictionary()  # Dictionary object
    time_dict = dictionary.time_dict()  # Time unit dictionary

    # Metric and Imperial distances
    if units_from in time_dict and units_to in time_dict:
        units_from_base = time_dict.get(
            units_from, None)  # Conversion to seconds
        units_to_base = time_dict.get(
            units_to, None)  # Conversion from seconds

        value = convert_time(value, units_from_base, units_to_base)
        return str(round(value, decimal_places)) + units_to

    return False


# DISTANCE, VOLUME, AND MASS/WEIGHT CONVERSION
# Convert Metric units to Imperial units
def metric_to_imperial(value, metric_base, imperial_base, imperial_multiplier):
    return value * metric_base * imperial_multiplier * imperial_base


# Convert Imperial units to Metric units
def imperial_to_metric(value, metric_base, imperial_base, metric_multiplier):
    return value * imperial_base * metric_multiplier / metric_base


def metric_to_metric(value, metric_base, metric_multiplier):
    return value * metric_base * metric_multiplier


# DIGITAL STORAGE CONVERSION
def check_digital_storage(value, units_from, units_to, decimal_places):
    dictionary = unit_dictionary.Dictionary()  # Dictionary object
    digital_storage_dict = dictionary.digital_storage_dict()  # Universal Metric unit dictionary

    # Digital storage conversions
    if units_from in digital_storage_dict and units_to in digital_storage_dict:
        from_base = digital_storage_dict.get(units_from, None)
        to_base = digital_storage_dict.get(units_to, None)

        value = value * from_base / to_base
        return str(round(value, decimal_places)) + units_to

    return False


def check_metric_imperial(value, units_from, units_to, decimal_places):
    dictionary = unit_dictionary.Dictionary()  # Dictionary object
    metric_dict = dictionary.metric_dict()  # Universal Metric unit dictionary
    imperial_dist_dict = dictionary.imperial_dist_dict()  # Imperial length dictionary
    imperial_vol_dict = dictionary.imperial_vol_dict()  # Imperial volume dictionary
    imperial_mass_dict = dictionary.imperial_mass_dict()  # Imperial mass dictionary

    # Removes the type of conversion: length (m), volume (l), mass (g)
    metric_units_from = units_from[
        0:len(units_from) -
        1] if len(units_from) > 1 else None
    metric_units_to = units_to[
        0:len(units_to) -
        1] if len(units_to) > 1 else None

    # Metric and Imperial distances
    if metric_units_from in metric_dict and units_to in imperial_dist_dict:
        metric_base = metric_dict.get(metric_units_from, None)
        imperial_base = imperial_dist_dict.get(units_to, None)
        value = metric_to_imperial(value, metric_base, imperial_base, 39.3701)
        return str(round(value, decimal_places)) + units_to
    elif units_from in imperial_dist_dict and metric_units_to in metric_dict:
        imperial_base = imperial_dist_dict.get(units_from, None)
        metric_base = metric_dict.get(metric_units_to, None)
        value = imperial_to_metric(value, metric_base, imperial_base, .0254)
        return str(round(value, decimal_places)) + units_to

    # Metric and Imperial volumes
    if metric_units_from in metric_dict and units_to in imperial_vol_dict:
        metric_base = metric_dict.get(metric_units_from, None)
        imperial_base = imperial_vol_dict.get(units_to, None)
        value = metric_to_imperial(value, metric_base, imperial_base, 33.814)
        return str(round(value, decimal_places)) + units_to
    elif units_from in imperial_vol_dict and metric_units_to in metric_dict:
        imperial_base = imperial_vol_dict.get(units_from, None)
        metric_base = metric_dict.get(metric_units_to, None)
        value = imperial_to_metric(value, metric_base, imperial_base, .0295735)
        return str(round(value, decimal_places)) + units_to

    # Metric and Imperial masses
    if metric_units_from in metric_dict and units_to in imperial_mass_dict:
        metric_base = metric_dict.get(metric_units_from, None)
        imperial_base = imperial_mass_dict.get(units_to, None)
        value = metric_to_imperial(
            value, metric_base, imperial_base, .00220462)
        return str(round(value, decimal_places)) + units_to
    elif units_from in imperial_mass_dict and metric_units_to in metric_dict:
        imperial_base = imperial_mass_dict.get(units_from, None)
        metric_base = metric_dict.get(metric_units_to, None)
        value = imperial_to_metric(value, metric_base, imperial_base, 453.592)
        return str(round(value, decimal_places)) + units_to

    return False


def convert_units(value, from_unit, to_unit, **args):
    """
    Takes the given value, source unit and target unit to convert.
    :param value: Value to convert
    :param from_unit: Source unit to convert from
    :param to_unit: Target unit to convert to
    :param args: Additional arguments important for conversion with multiple dependencies
    :return:
    """

    # Check if units can be converted
    if not can_convert(from_unit, to_unit):
        return '[!] Units cannot be converted\n'

    # Extract the numeric value from the string
    decimal_places = 2  # Set the default value of precision
    if "." in str(value):
        decimal_places = len(str(value)[str(value).index('.') + 1:])

    # Return the value if units are the same
    if from_unit == to_unit:
        return str(value) + " " + get_si(to_unit)

    responses = [
        check_time(value, from_unit, to_unit, decimal_places),  # Time units
        check_metric_imperial(
            value,
            from_unit,
            to_unit,
            decimal_places),  # Metric and Imperial units
        check_digital_storage(
            value,
            from_unit,
            to_unit,
            decimal_places
        )  # Digital storage units
    ]

    for response in responses:
        if response:
            return response

    # actually convert the units
    try:
        return str(round(convert(from_unit, to_unit, float(value), **args), decimal_places)) + " " + get_si(to_unit)
    except RequireAdditionalParamError as e:
        return handle_additional_required_params(e.additional_params)
    except ConversionError as e:
        print(e.reason)
