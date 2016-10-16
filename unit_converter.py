import sys
import unit_dictionary
from converters import convert, can_convert, get_si
from converters.ConversionError import ConversionError
from converters.RequireAdditionalParamError import RequireAdditionalParamError


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


# Check if the input is valid
def check_input(s):
    if len(str(s).split('/')) == 3:
        return True
    else:
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
    decimal_places = 2 # Set the default value of precision
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
        additional_unit = input("\n[*] Enter an additional unit (choose between " + str(e.additional_params) + "): ")
        additional_value = float(input("\n[*] Enter the value: "))
        return convert_units(value, from_unit, to_unit, **{additional_unit: additional_value})
    except ConversionError as e:
        print(e.reason)


def input_dialog():
    from_unit = input('\n[*] Enter a unit to convert from: ')

    if from_unit == 'exit':
        print('[-] Program exited.')
        sys.exit(0)

    to_unit = input('\n[*] Enter a unit to convert to: ')

    if to_unit == 'exit':
        print('[-] Program exited.')
        sys.exit(0)

    value = input(str('\n[*] Enter a value to convert from {0} to {1}: ').format(get_si(from_unit), get_si(to_unit)))

    if value == 'exit':
        print('[-] Program exited.')
        sys.exit(0)

    return from_unit, to_unit, value


if __name__ == '__main__':
    # The rest of the code is just here for testing purposes
    # Information about the script
    print('Python unit converter by mattgd.\n \
        \nUnits supported:\n \
        Circle\t\t: radians (rad), degrees (deg) \n \
        Temperature\t: Celsius (c), Fahrenheit (f), and Kelvin (k) \n \
        Speed\t\t: Kilometers/hour (kph), miles/hour (mph), knots(kt) .')
    print('\n\n[-] Example entries: 1.345/rad/degrees, 33/f/c, 2/mph/kph')
    print('\n\n[-] To close type "exit"')

    number = 0
    while number != 'exit':
        # Bind raw_input to input for both Python2 and Python3 compatibility
        try:
            input = raw_input
        except NameError:
            pass

        # Ask user for a number
        from_unit, to_unit, value = input_dialog()

        # Display the converted number
        print(convert_units(value, from_unit, to_unit))
        print("\n") # make clear that a new conversion begun
