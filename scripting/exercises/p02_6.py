# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 09:32:01 2017

@author: ksagilop

6 Plot Trigonometry

Creating real graphical output
This exercise is different from the previous ones in that 
you will get a complete script and are asked to make it run and
play with it in order to understand it. 

You are not supposed to know how to do this already. In fact, you don’t. 
When programming, you will often face such new 
(and somewhat scary) situations, but with time you learn that you have 
the ability to work through them. This is just a training occasion 
for such situations. You are not obliged to produce any outcome here; but we
estimate that with 1-2 hours investment of time you would 
figure out the script completely. 

Let’s give it a try and see what you can achieve in 15 minutes?
There are two challenges here:

1. Make it run.
First, here’s the script:
"""

# Modules
import numpy as np
import pylab as pl

#Constants
n = 256

X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Ysin = np.sin(2 * X)
Ycos = np.cos(2 * X)

#pl.axes([0.025, 0.025, 0.95, 0.95])
pl.plot(X, Ysin, color='blue', alpha=1.00)
pl.plot(X, Ycos, color='green', alpha=1.00)
pl.xlim([-np.pi, np.pi])
pl.ylim([-2.5, 2.5])
pl.show()

"""
2. Understand what’s going on.
Ideas for finding out what the code does are:
    
* Manipulate individual lines and observe what happens if you re-run the script
(e.g., change the values of “parameters”)

* Render certain lines ineffective by commenting them out (:= putting a “#” at the
start of a line so the code will be regarded as a comment by Python) and observe
what they contribute to the overall script

*Do a web search for certain key words that appear in the code

*Use pdb to debug the script step by step

*Read on plotting with Python:
https://help.uis.cam.ac.uk/help-support/training/
downloads/coursefiles/programming-student-files/python-courses/
pythontopics/pythontopicsfiles/graphs.pdf
"""