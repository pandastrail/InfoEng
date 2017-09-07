# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 12:41:12 2017

@author: ksagilop

Simple Graphs Tutorial using pylab
"""
# Modules
import numpy as np
import matplotlib.pyplot as plt

# Data
x = [0,1,2,3,4,5]
y = [3,10,15,17,22,23]
z = [4,7,2,21,15,18]
k = [10,15,45,12,30,85]
m = [10,52,60,30,80,125]

# Plot
plt.title('Simple Graph Line example')
plt.xlabel('This is label x')
plt.ylabel('This is label y')
#pl.axis([-1,5,-1,25])
plt.scatter(x,y, c=m, s=k, label='label 1')
plt.scatter(x,z, s=k, label='label 2')
#pl.plot(x,z, 'ro', label='set 2')
plt.legend(title='La Leyenda')
plt.show()

# Or
#pl.plot(x,y, color='green', linestyle='dashed', marker='o',
#         markerfacecolor='blue', markersize=12)
#pl.show()
