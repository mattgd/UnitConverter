import sys
import math
import unit_dictionary

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

# ELECTRIC CONVERSION

# Watts to Amps
def w_to_a(watts, volts):
    return watts / volts

# Watts to Volts
def w_to_v(watts, amps):
    return watts / amps

# Watts to Ohms given Amps
def w_to_o(watts, amps):
    return watts / (amps * amps)

# Watts to Ohms given Volts
def w_to_o2(watts, volts):
    return (volts * volts ) / watts

# Watts to Joules given time
def w_to_j(watts, seconds):
    return watts * seconds

# Watts to Horsepower
def w_to_hp(watts):
    return watts * 746

# TIME CONVERSION
def convert_time(value, units_from_base, units_to_base):
    return value * units_from_base / units_to_base

def check_time(value, units_from, units_to, decimal_places):
    dict = unit_dictionary.dictionary() # Dictionary object
    time_dict = dict.time_dict() # Time unit dictionary

    # Metric and Imperial distances
    if units_from in time_dict and units_to in time_dict:
        units_from_base = time_dict.get(units_from, None) # Conversion to seconds
        units_to_base = time_dict.get(units_to, None) # Conversion from seconds

        value = convert_time(value, units_from_base, units_to_base)
        return str(round(value, decimal_places)) + units_to

    return False

# DISTANCE CONVERSION
# Convert Metric units to Imperial units
def metric_to_imperial(value, metric_base, imperial_base, imperial_multiplier):
    return value * metric_base * imperial_multiplier * imperial_base
# Convert Imperial units to Metric units
def imperial_to_metric(value, metric_base, imperial_base, metric_multiplier):
    return value * imperial_base * metric_multiplier / metric_base

def check_metric_imperial(value, units_from, units_to, decimal_places):
    dict = unit_dictionary.dictionary() # Dictionary object
    metric_dict = dict.metric_dict() # Universal Metric unit dictionary
    imperial_dist_dict = dict.imperial_dist_dict() # Imperial length dictionary
    imperial_vol_dict = dict.imperial_vol_dict() # Imperial volume dictionary
    imperial_mass_dict = dict.imperial_mass_dict() # Imperial mass dictionary

    metric_base = None
    imperial_base = None

    # Removes the type of conversion: length (m), volume (l), mass (g)
    metric_units_from = units_from[0:len(units_from) - 1] if len(units_from) > 1 else None
    metric_units_to = units_to[0:len(units_to) - 1] if len(units_to) > 1 else None

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
        value = metric_to_imperial(value, metric_base, imperial_base, .00220462)
        return str(round(value, decimal_places)) + units_to
    elif units_from in imperial_mass_dict and metric_units_to in metric_dict:
        imperial_base = imperial_mass_dict.get(units_from, None)
        metric_base = metric_dict.get(metric_units_to, None)
        value = imperial_to_metric(value, metric_base, imperial_base, 453.592)
        return str(round(value, decimal_places)) + units_to

    return False

# Takes in a parameter s, the value and the unit to convert from/to
def convert_units(s):
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

    # Return the value if units are the same
    if units_from == units_to:
        return str(value) + units_to

    responses = [
        check_time(value, units_from, units_to, decimal_places), # Time units
        check_metric_imperial(value, units_from, units_to, decimal_places) # Metric and Imperial units
    ]

    for response in responses:
        if response != False:
            return response

    # Check the rest of the conversion factors
    # Get proper method for conversion
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
