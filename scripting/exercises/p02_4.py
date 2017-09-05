# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:36:32 2017

@author: ksagilop

4 Litres to Kilograms

Another conversion task
Write a small program that asks the quantity (in litres l) 
and density (:= mass per volume in kg/l) of some fluid from the user 
via the console and outputs the weight of it in kilograms.

The code and formulae is going to be rather simple; 
can you already guess it given the
units of the two inputs? Otherwise, look it up on the web.
"""
# Functions
def weight(v,d):
    w = v*d
    print('Weight is equal to ', "%.2f" % w, 'kg')
    return w

# Input
v = float(input('Volume in liters l? '))
d = float(input('Density in kg/l? '))

# Execute
weight(v,d)