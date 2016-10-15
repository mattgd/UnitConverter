# -*- coding: utf-8 -*-
from ConversionError import ConversionError


# Watts to Amps
def watts_to_amps(watts, volts):
    return watts / volts


# Watts to Volts
def watts_to_volts(watts, amps):
    return watts / amps


# Watts to Ohms given Amps or Volts
def watts_to_ohms(watts, amps = None, volts = None):
    if amps is not None:
        return watts / (amps * amps)
    elif volts is not None:
        return (volts * volts) / watts
    else:
        raise ConversionError("The second given param was not specified correctly. A conversion is not possible.")


# Watts to Joules given time
def watts_to_joules(watts, seconds):
    return watts * seconds


# Watts to Horsepower
def watts_to_horsepower(watts):
    return watts * 746


# Watts to BTUs per second (BTU/s)
def watts_to_btups(watts):
    return watts * 0.00095  # Precision of 5 significant digits


# Watts to Calories per second (cal/s)
def watts_to_cal(watts):
    return watts * 0.23885  # Precision of 5 significant digits
