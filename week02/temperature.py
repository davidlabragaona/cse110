"""
Author: David Labra Gaona
Date: 28 APR 2023
Time: 05:45

Purpose: The following program converts from Farenheit to Celsius
It displays the result to one decimal place of precision.

To convert degrees in Fahrenheit to Celsius you need to subtract 32
from the Fahrenheit amount and then multiply it by the fraction 5/9.

"""

# We ask the user to enter the temperature
farenheit = input('What is the temperature en Farenheit? ')

# Celsius = (farenheit - 32) * 5 / 9
celsius = (int(farenheit) - 32) * (5/9)

# One decimal digit format specifier {:.1f}
print('The temperature in Celsius is {:.1f} degress.'.format(celsius))
