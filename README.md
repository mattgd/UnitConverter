<!--# UnitConverter-->
<h1><a href="https://github.com/mattgd/UnitConverter" target="_blank"><img width="175" src="http://www.mattd.xyz/unitconverter/logo-color.png"></a></h1>
A unit conversion API module in Python.

###Requirements
* **Python2 & above**

### Supported Units and Categories
| Category    | Units                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Angles of Circles | radians (rad), degrees (deg)                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Temperature       | Celsius (C), Fahrenheit (F), Kelvins (K)                                                                                                                                                                                                                                                                                                                                                                                                 |
| Distance          | Metric distances: attometer (am), femtometer (fm), picometer (pm), nanometer (nm), micrometer (μm), milimeter (mm), centimeter (cm), decimeter (dm), meter (m), decameter (dam), hectometer (hm), kilometer (km), megameter (Mm), gigameter (Gm), terameter (Tm), petameter (Pm), exameter (Em) Imperial distances: thou (th), inch (in), link (li), foot (ft), yard (yd), rod (rod), chain (ch), furlong (fur), mile (mi), league (lea) |
| Volume            | Metric volumes: attoliter (al) to exaliter (El) Imperial volumes: fluid ounce (floz), gill (gi), pint (pt), quart (qt), gallon (gal)                                                                                                                                                                                                                                                                                                     |
| Mass and Weight   | Metric mass: attoggram (ag) to Exagram (Eg) Imperial mass: grain (gr), drachm (dr), ounce (oz), pound (lb), stone (st), quarter (qtr or qr), hundredweight (cwt), ton (t)                                                                                                                                                                                                                                                                |
| Time              | yocotosecond (ys), zeptosecond (zs), attosecond (as), femtosecond (fs), picosecond (ps), nanosecond (ns), microsecond (µs), milisecond (ms), cs, ds, second (s), minute (min), kilosecond (ks), hour (hr), day (day), week (wk), megasecond (Ms), month (mo), year (yr), gigasecond (Gs), terasecond (Ts), petasecond (Ps), exasecond (Es), Zs, Ys                                                                                       |
| Pressure          | pascal (pa), torr (torr), pounds per square inch (psi), bar (bar), technical atmosphere (at), atmosphere (atm)                                                                                                                                                                                                                                                                                                                           |
| Energy            | watt (w), joule (j), horsepower (hp), Calorie (cal), British thermal unit (btu)                                                                                                                                                                                                                                                                                                                                                          |
| Speed             | kilometers per hour (kph), miles per hour (mph), knots (kt)                                                                                                                                                                                                                                                                                                                                                                              |
| Force             | Newton (N), dyne (dyn), Kilogram-Force (kp), Poundal (pdl)                                                                                                                                                                                                                                                                                                                                                                               |
| Digital Storage   | bit (bit), byte (byte), kilobyte (kB), megabyte (MB), gigabyte (GB), terabyte (TB), petabyte (PB), exabyte (EB), zettabyte (ZB), yottabyte (YB)                                                                                                                                                                                                                                                                |

###Examples

```python
UnitConverter $ python unit_converter.py
Python unit converter by mattgd.
     Units supported:
     Circle: radians (rad), degrees (deg)
     Temperature: Celsius (c), Fahrenheit (f), and Kelvin (k)
     Speed: Kilometers/hour (kph), miles/hour (mph), knots(kt) .
Example entries: 1.345/rad/deg, 33/f/c, 2/mph/kph
Enter a unit to convert from: F
Enter a unit to convert to: C
Enter a value to convert from F to C:
37.8 °C
Enter a unit to convert from: kt
Enter a unit to convert to: mph
Enter a value to convert from Kn to mph: 3
3.5 mph
Enter a unit to convert from: W
Enter a unit to convert to: O
Enter a value to convert from W to Ω: 12
Enter an additional unit (choose between ['A', 'V']): V
Enter the value: 12
12 Ω
```

###Contributing to This Repository

If you'd like to contribute, feel free to make changes or additions and submit a pull request. Below are two full example methods:
```
# Watts to Horsepower
def w_to_hp(watts):
    return watts * 746
```
```
# Pa to psi
def Pa_to_psi(value):
    return value / 6894.76
```
Please create new converter files for new conversion sections and use existing ones for the conversion.

If you have created a new file for new conversion sections don't forget to include all functions into the `__init__.py` in the `converters` module and create an entry in the `UNITS` array in the `converters.Converter` file

Note that the method name should include the proper abbreviation casing instead of conventional casing for Python. Also, you may use the name of the unit being converted from as the variable.
