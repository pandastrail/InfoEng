# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 14:02:56 2017

@author: ksagilop

2 Celsius to Fahrenheit
Convert degrees Celsius to degrees Fahrenheit

Write a program that reads a temperature in Celsius from the console 
and converts it into degrees Fahrenheit.

*The temperature T in degrees Fahrenheit (°F) 
is equal to the temperature T in degrees Celsius (°C) times 9/5 plus 32

*http://www.rapidtables.com/convert/temperature/how-celsius-to-fahrenheit.htm
"""
# Functions
def temp(c):
    f = (c * (9/5)) + 32
    print('Temp in Fahrenheit is ', "%.1f" % f, 'F') # Float point to 1-digit
    return f

# Reads a floating point number from keyboard input 
# and stores it in a variable named “v0”:
c = float(input('degrees Celsius? '))

# Execute
temp(c)