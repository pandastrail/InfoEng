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

# Functions
def braking(v0, mu):
    