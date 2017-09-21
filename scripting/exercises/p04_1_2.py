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
import math

# Assigments
x_point = []
y_point = []
d = []

'''
xy_points = ({1: {'x': 1, 'y': 1},
              2: {'x': 2, 'y': 1},
              3: {'x': 1, 'y': 2},
              4: {'x': 1, 'y': 1},
              })
'''
    
xy_points = ({1: {'x':142.492, 'y': 208.536},
              2: {'x':142.658, 'y': 207.060},
              3: {'x':143.522, 'y': 205.978},
              4: {'x':145.009, 'y': 205.546},
              5: {'x':146.492, 'y': 204.536},
              6: {'x':147.658, 'y': 203.060},
              7: {'x':148.522, 'y': 202.978},
              8: {'x':149.009, 'y': 201.546},
              })
    
#print(xy_points)
# Distance is equal to 4.41
for i in range(1, len(xy_points)+1):
    xy_point = xy_points[i]
    #print(xy_point)
    x_point.append(xy_point['x'])
    y_point.append(xy_point['y'])
    
for i in range(1,len(xy_points),1):
    print('i: ', i)
    x = (xy_points[i+1]['x'] - xy_points[i]['x'])**2
    print(xy_points[i+1]['x'], '-', xy_points[i]['x'], '**2')
    
    y = (xy_points[i+1]['y'] - xy_points[i]['y'])**2
    print(xy_points[i+1]['y'], '-', xy_points[i]['y'], '**2')
    
    d_partial = math.sqrt(x+y)
    d.append(d_partial)

print('partial distances: ', d)
d_total = sum(d)
print('total_distance: ', d_total)
#print('x: ', x_point)
#print('y: ', y_point)
plt.plot(x_point, y_point)
plt.show()