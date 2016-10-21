# -*- coding: utf-8 -*-
from converters.circle import circle
from converters.currency import currency
from converters.electric import electric
from converters.force import force
from converters.pressure import pressure
from converters.speed import speed
from converters.temperature import temperature


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
