# -*- coding: utf-8 -*-
from UnitConverter.converters.circle import circle
from UnitConverter.converters.currency import currency
from UnitConverter.converters.electric import electric
from UnitConverter.converters.force import force
from UnitConverter.converters.pressure import pressure
from UnitConverter.converters.speed import speed
from UnitConverter.converters.temperature import temperature


class UnitsManager(object):
    '''
    Class responsible to manage the unit converters
    of this application.
    '''
    _units = [
        circle,
        currency,
        electric,
        force,
        pressure,
        speed,
        temperature,
    ]

    def __iter__(self):
        return (x for x in self._units)

    def register(self, converter):
        """
        Method that receives a new converter and adds it to
        this manager.
        Useful to add custom new methods without needing to edit
        the core of this application.
        """
        if converter is not None and callable(converter):
            self._units.append(converter)


UNITS = UnitsManager()
