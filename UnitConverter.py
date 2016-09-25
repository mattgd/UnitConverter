import sys
import math

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
# Centimeters and inches
def cm_to_in(value):
    return value * .393701
def in_to_cm(value):
    return value / .393701

# Inches and feet
def in_to_ft(value):
    return value / 12
def ft_to_in(value):
    return value * 12

# Meters and feet
def m_to_ft(value):
    return value * 3.28084
def ft_to_m(value):
    return value / 3.28084

# TODO Come up with a better way to convert between Metric system units
# Centimeters and meters
def cm_to_m(value):
    return value * .01
def m_to_cm(value):
    return value / .01

# Centimeters and feet
def cm_to_ft(value):
    return in_to_ft(cm_to_in(value))
def ft_to_cm(value):
    return in_to_cm(ft_to_in(value))

# Meters and inches
def m_to_in(value):
    return ft_to_in(m_to_ft(value))
def in_to_m(value):
    return ft_to_m(in_to_ft(value))

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
