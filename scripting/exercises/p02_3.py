# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 16:42:00 2017

@author: ksagilop

3 Distance between to aircrafts

Create a program that reads the 2D coordinates (x, y) from two planes 
from the console and computes their distance.

You can use the standard Euclidean distance as a distance measure: 
It is the square root of the sum of the squared differences
between the respective x- and y coordinates.

Hint – In Python, you can use a build-in function to compute the square root:
#compute the square root of a quantity (number) a and 
store it in a variable square_root_of_a:
    
import math
square_root_of_a = math.sqrt(a)

"""
# Import modules
import math

# Functions
def dist(x1, y1, x2, y2):
    '''Compute 2D euclidean distance'''
    x = (x2 - x1)**2  # Compute square sum of x-coordinates
    y = (y2 - y1)**2  # Compute square sum of y-coordinates
    d = math.sqrt(x + y)  # square root of sum
    print ('Distance between two-points is', "%.2f" % d)
    return d

# Input
x1 = float(input('x1? '))
y1 = float(input('y1? '))
x2 = float(input('x2? '))
y2 = float(input('y2? '))

# Execute
dist(x1, y1, x2, y2)

'''May refine input by getting it in the form (x1,y1)'''