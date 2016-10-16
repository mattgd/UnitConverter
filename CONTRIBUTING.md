# Contributing to This Repository

If you'd like to contribute, feel free to make changes or additions and submit a pull request.

Please create new converter files for new conversion sections and use existing ones for the conversion. Take a look at other files in the `converters` directory for a template on creating a new conversion section.

If you have created a new file for new conversion sections don't forget to include all functions into the `__init__.py` in the `converters` module and create an entry in the `UNITS` array in the `converters.Converter` file

Note that the method name should include the proper abbreviation casing instead of conventional casing for Python. Also, you may use the name of the unit being converted from as the variable.
