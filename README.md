# UnitConverter
A unit conversion API module in Python.

####Requirements:
**Python3**

####Supported conversions:
* Temperature
* Angles of Circle
* Speed

####Units:
* Angles of Circle:  __radians (r), degrees (d)__
* Temperature:       __Celsius (c), Fahrenheit (f), and Kelvin (k)__
* Speed:                 __Kilometers/hour (kph), miles/hour (mph), knots(kt)__

####Examples:

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
