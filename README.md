# UnitConverter
A unit conversion API module in Python.

###Requirements
* **Python2 & above **

### Supported Units and Categories
| Category    | Units                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Angles of Circles | radians (r), degrees (d)                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Temperature       | Celsius (C), Fahrenheit (F), Kelvins (K)                                                                                                                                                                                                                                                                                                                                                                                                 |
| Distance          | Metric distances: attometer (am), femtometer (fm), picometer (pm), nanometer (nm), micrometer (μm), milimeter (mm), centimeter (cm), decimeter (dm), meter (m), decameter (dam), hectometer (hm), kilometer (km), megameter (Mm), gigameter (Gm), terameter (Tm), petameter (Pm), exameter (Em) Imperial distances: thou (th), inch (in), link (li), foot (ft), yard (yd), rod (rod), chain (ch), furlong (fur), mile (mi), league (lea) |
| Volume            | Metric volumes: attoliter (al) to exaliter (El) Imperial volumes: fluid ounce (floz), gill (gi), pint (pt), quart (qt), gallon (gal)                                                                                                                                                                                                                                                                                                     |
| Mass and Weight   | Metric mass: attoggram (ag) to Exagram (Eg) Imperial mass: grain (gr), drachm (dr), ounce (oz), pound (lb), stone (st), quarter (qtr or qr), hundredweight (cwt), ton (t)                                                                                                                                                                                                                                                                |
| Time              | yocotosecond (ys), zeptosecond (zs), attosecond (as), femtosecond (fs), picosecond (ps), nanosecond (ns), microsecond (µs), milisecond (ms), cs, ds, second (s), minute (min), kilosecond (ks), hour (hr), day (day), week (wk), megasecond (Ms), month (mo), year (yr), gigasecond (Gs), terasecond (Ts), petasecond (Ps), exasecond (Es), Zs, Ys                                                                                       |
| Pressure          | pascal (pa), torr (torr), pounds per square inch (psi), bar (bar), technical atmosphere (at), atmosphere (atm)                                                                                                                                                                                                                                                                                                                           |
| Energy            | watt (w), joule (j), horsepower (hp), Calorie (cal), British thermal unit (btu)                                                                                                                                                                                                                                                                                                                                                          |
| Speed             | kilometers per hour (kph), miles per hour (mph), knots (kt)                                                                                                                                                                                                                                                                                                                                                                              |
| Force             | Newton (N), dyne (dyn)                                                                                                                                                                                                                                                                                                                                                                               |

###Examples

```python
UnitConverter $ python unit_converter.py
Python unit converter by mattgd.
     Units supported:
     Circle: radians (r), degrees (d)
     Temperature: Celsius (c), Fahrenheit (f), and Kelvin (k)
     Speed: Kilometers/hour (kph), miles/hour (mph), knots(kt) .
Example entries: 1.345/r/d, 33/f/c, 2/mph/kph
Enter a value and units to covert from and to: 100/f/c
37.8c
Enter a value and units to covert from and to: 3/kt/mph
3.5mph
Enter a value and units to covert from and to: 4/kt/mph
4.6mph
```
