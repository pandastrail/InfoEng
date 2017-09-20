#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:23:39 2017

@author: hase

1.2 Trail Length
Write a program that computes the total length of a trail tracked 
with your GPS device. Let’s assume your GPS device saves your 
coordinates every 5 second into a list of tuples.

For the trail in the right image above, the list of tuples would look like this:
trail = [(142.492, 208.536),
(142.658, 207.060),
(143.522, 205.978),
(145.009, 205.546)]

Create a function pathlength(trail) for computing L according to the formula
above (see pdf). The argument trail should be a list of (x,y) coordinate tuples. 
Test the function on a triangular path with the four points 
(1, 1), (2, 1), (1, 2), and (1, 1).

Hint: To compute the square root of some value x, use import math
math.sqrt(x)
distance = sqrt((x2-x1)**2 + (y2-y1)**2)

Or use scipy.spatial.distance.cdist? or pdist?
"""
# Modules
import numpy as np
import matplotlib.pyplot as plt

# Assigments
x_point = []
y_point = []

xy_points = (1, 1), (2, 1), (1, 2), (1, 1)
# Distance is equal to 4.41
for i in range(len(xy_points)):
    xy_point = xy_points[i]
    x_point.append(xy_point[0])
    y_point.append(xy_point[1])

print('x: ', x_point)
print('y: ', y_point)
plt.plot(x_point, y_point)
plt.show()