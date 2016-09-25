import sys
import math
import unit_dictionary

# Convert from degrees to radians or vice versa
temperature = ['c', 'f', 'k']
circle = ['d', 'r']
distance = ['cm', 'm', 'in', 'ft']

# TEMPERATURE CONVERSION
# Celsius and Fahrenheit
def c_to_f(value):
    return value * 1.8 + 32
def f_to_c(value):
    return (value - 32) / 1.8

# Celsius and Kelvin
def c_to_k(value):
    return value + 273.15
def k_to_c(value):
    return value - 273.15

# Fahrenheit and Kelvin
def f_to_k(value):
    return c_to_k(f_to_c(value))
def k_to_f(value):
    return c_to_f(k_to_c(value))

# CIRCLE CONVERSION
# Radians and degress
def r_to_d(value):
    return math.degrees(value)
def d_to_r(value):
    return math.radians(value)

# DISTANCE CONVERSION
# Convert Metric units to Imperial units
def metric_to_imperial(value, metric_base, imperial_base, imperial_multiplier):
    return value * metric_base * imperial_multiplier * imperial_base
# Convert Imperial units to Metric units
def imperial_to_metric(value, metric_base, imperial_base, metric_multiplier):
    # 7.628 in / 1 * metric_multiplier / 1
    return value * imperial_base * metric_multiplier / metric_base

# Takes in a parameter s, the value and the unit to convert from/to
def convert_units(s):
    s = s.lower() # Convert to lower case for easier use

    # Ensure valid input: value/unitfrom/unitto
    try:
        s.index('/')
    except ValueError:
        return 'Invalid input. Format: value/unitfrom/unitto\n'

    value = float(s[0:s.index('/')]) # Extract the numeric value from the string
    decimal_places = len(str(value)[str(value).index('.') + 1:])
    units = s[s.index('/') + 1:] # Extract the units from the string

    # Ensure valid units input: unitfrom/unitto
    try:
        units.index('/')
    except ValueError:
        return 'Invalid input. Format: value/unitfrom/unitto\n'

    units_from = units[0:units.index('/')] # Everything before the slash is from
    units_to = units[units.index('/') + 1:] # Everything after the slash is to

    # Metric and Imperial distance conversion
    metric_dist_dict = unit_dictionary.metric_dict() # Metric unit dictionary
    imperial_dist_dict = unit_dictionary.imperial_dict() # Imperial unit dictionary

    metric_base = None
    imperial_base = None
    if units_from in metric_dist_dict and units_to in imperial_dist_dict:
        metric_base = metric_dist_dict.get(units_from, None)
        imperial_base = imperial_dist_dict.get(units_to, None)
        value = metric_to_imperial(value, metric_base, imperial_base, 39.3701)
        return str(round(value, decimal_places)) + units_to
    elif units_from in imperial_dist_dict and units_to in metric_dist_dict:
        imperial_base = imperial_dist_dict.get(units_from, None)
        metric_base = metric_dist_dict.get(units_to, None)
        value = imperial_to_metric(value, metric_base, imperial_base, .0254)
        return str(round(value, decimal_places)) + units_to

    # Return the value if units are the same
    if units_from == units_to:
        return str(value) + units_to

    conversion_method = units_from + '_to_' + units_to # Name of method to use
    thismodule = sys.modules[__name__] # This module as object

    try:
        value = getattr(thismodule, conversion_method)(value)
        return str(round(value, decimal_places)) + units_to
    except AttributeError:
        return 'Incompatible units.'

# The rest of the code is just here for testing purposes
# Information about the script
print('Python unit converter by mattgd.\nUnits supported radians (r), degrees (d), Celsius (c), Fahrenheit (f), and Kelvin (k).')
print('Example entries: 1.345rd, 33fc')

number = 0
while number != 'exit':
    # Ask user for a number
    number = input('Enter a value and units to covert from and to: ')

    if number == 'exit':
        print('Program exited.')
        break

    # Display the converted number
    print(convert_units(number))
