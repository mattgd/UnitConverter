# -*- coding: utf-8 -*-


def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit
    """
    return celsius * 1.8 + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius
    """
    return (fahrenheit - 32) / 1.8


def celsius_to_kelvin(celsius):
    """
    Convert Celsius to Kelvin
    """
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    """
    Convert Celsius to Kelvin
    """
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    """
    Convert Fahrenheit to Kelvin
    """
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))


def kelvin_to_fahrenheit(kelvin):
    """
    Convert Kelvin to Fahrenheit
    """
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))
