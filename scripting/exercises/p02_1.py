# -*- coding: utf-8 -*-
"""
P02 Excercises

1. Braking Distance
Compute the distance it takes to stop a car

A car driver, driving at velocity v0, suddenly puts on the brake. 
What braking distance d is needed to stop the car?

One can derive, from basic physics, that
    d = 0.5*v0^2 / (mu*g)

Compute d with a given velocity v0 and friction coefficient mu 
via the raw_input function. g is of course known

Run the program for two cases:
    v0 = 120 km/h and
    v0 = 50 km/h, both with mu = 0.3 (mu is dimensionless)

Remember to convert the velocity from km/h to m/s before inserting 
the value in the formula!
"""

# Constants
g = 9.8  # Gravitational constant in m/s^2

# Functions
def braking(v0, mu):
    v0 = (v0*1000)/3600 # Convert km/h to m/s
    d = 0.5*v0**2 / (mu*g) # Compute distance to braking
    print('Distance to brake is ', "%.2f" % d, 'm') # Float point to 2 digits
    return d

# Reads a floating point number from keyboard input 
# and stores it in a variable named “v0”:
v0 = float(input('v0 [km/h]? '))
mu = float(input('mu [friction coef]? ')) 

# Execute
braking(v0, mu)