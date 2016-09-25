import math

# Convert from degrees to radians or vice versa
temperature = ['c', 'f', 'k']
circle = ['d', 'r']

def celsiusToFahrenheit(temp):
    return temp * 1.8 + 32

def fahrenheitToCelsius(temp):
    return (temp - 32) / 1.8

def celsuisToKelvin(temp):
    return temp + 273.15

def kelvinToCelsius(temp):
    return temp - 273.15

def radiansToDegrees(value):
    return math.degrees(value)

def degreesToRadians(value):
    return math.radians(value)

def convert(number):
    number = number.lower()
    value = float(number[0:-2])
    unitsFrom = number[-2:-1]
    unitsTo = number[-1:]

    if unitsFrom in temperature and unitsTo in temperature:
        if unitsFrom == 'c' and unitsTo == 'f':
            value = celsiusToFahrenheit(value)
        elif unitsFrom == 'c' and unitsTo == 'k':
            value = celsuisToKelvin(value)
        elif unitsFrom == 'f' and unitsTo == 'c':
            value = fahrenheitToCelsius(value)
        elif unitsFrom == 'f' and unitsTo == 'k':
            value = celsuisToKelvin(fahrenheitToCelsius(value))
        elif unitsFrom == 'k' and unitsTo == 'c':
            value = kelvinToCelsius(value)
        elif unitsFrom == 'k' and unitsTo == 'f':
            value = celsiusToFahrenheit(kelvinToCelsius(value))
    elif unitsFrom in circle and unitsTo in circle:
        if unitsFrom == 'r':
            value = radiansToDegrees(value)
        elif unitsFrom == 'd':
            value = degreesToRadians(value)
    else:
        return 'Incompatible units.'

    return str(round(value, 2)) + unitsTo

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
    print(convert(number))
