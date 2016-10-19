# Contributing to This Repository

If you'd like to contribute, feel free to make changes or additions and submit a pull request.

Please create new converter files for new conversion sections and use existing ones for the conversion. Take a look at other files in the `converters` directory for a template on creating a new conversion section.

If you have created a new file for new conversion sections don't forget to include the new conversion-array to the `UNITS` array in the `converters.Converter` file otherwise the changes won't be visible to the system.

Note that the array should contain a name to indicate the conversion category and all units that can be converted.

A sample is listed below.

```
{
    "name": "Temperature",
    "units": [
        {
            "name": "Celsius",
            "si": "°C",
            "_internal_accepted_names": [
                "c",
                "celsius",
                "°c",
            ],
            "_internal_function_": "celsius",
            "_internal_conversion": {
                "fahrenheit": lambda celsius: celsius * 1.8 + 32,  # celsius to fahrenheit
                "kelvin": lambda celsius: celsius + 273.15,  # celsius to kelvin
            },
        },
        ...
    ],
}
```

In the sample we see that the `Temperature` has (at least) one unit (`Celsius`). To convert from or to celsius the input "c", "celsius" and "°c" are allowed in the terminal (case insensitive).

To allow one conversion an entry into the "_internal_conversion" array has to be inserted. The key of the entry should be the "_internal_function_" value of the target unit. The value displays a function which will get executed with at least the value to convert from. If additional parameters are required simply add them and set them default to `None`. The function resolver will automatically ask the user to enter the needed parameters. (Currently tested with electric conversions and one additional parameter and with two additional parameters where only one will get used -> Maybe the function resolver needs to be changed in order to use more than one additional parameter).

To indicate the result the "si" value needs to be filled. This filed displays the si-value and will be appended on the result value. (So the result of converting 273.15 Kelvin into Celsius is not only 0 but 0 °C)
