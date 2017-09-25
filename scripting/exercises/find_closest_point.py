#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:44:42 2017

@author: hase

Find closest point
- There is a board with (x,y) points
- The user input a (x,y) point
- The program returns the closest point to the one given and the distance
between them
"""
# Modules
import matplotlib.pyplot as plt
import numpy as np

# Functions
def galaxy(dots):
    '''Generate a n x 2 random array using numpy.random
    This will be the board of points to compare the user input'''
    coord_array =  np.random.random_sample((dots, 2)) * 10
    # random sample multiplied by 10 to get pairs between 0 and 10
    coord_list = list(coord_array)
    return coord_list

def closest(coordinates):
    ''' Calculate closest point to a given coordinates and the
    distance between this closest point and the given coordinates.
    It outputs the first closest point found.
    What if there are more than one closest point'''
    if type(coordinates) != type([]):
        raise Exception('Coordinates must have a type list')
    # The exception defined above is no longer valid after np.random
    point = None
    distance = None
    x = []
    y = []
    for k in coordinates:
        x.append(k[0])          # Append to list of x's to plot
        y.append(k[1])          # Append to list of y's to plot
        if k is None: continue
        # And calculate euclidean distance:
        d = (((k[0] - goal[0])**2 + (k[1] - goal[1])**2) ** 0.5)  # alt for math.sqrt
        if point is None or d < distance:   # Reassign if needed
            point = k
            distance = d
    return point, distance, x, y

def user():
    '''Get user coordinates and transform to tuple.
    Needs to be optimized to accept float
    and accept values larger than 9'''
    goal_list = []
    goal_raw = input('your x,y coordinates? ')
    goal_list.append(int(goal_raw[0]))
    goal_list.append(int(goal_raw[2]))
    goal = tuple(goal_list)
    return goal
    
# Execute
goal = user()
dots = int(input('How many points to draw? '))  # Needs try and except
coord_list = galaxy(dots)
point, distance, x, y = closest(coord_list)
plt.scatter(x,y)
plt.scatter(goal[0], goal[1], s=100)
plt.show()
print('Point given', goal, 'is closest to:')
print('point', point, 'with distance', "%.2f" % distance)