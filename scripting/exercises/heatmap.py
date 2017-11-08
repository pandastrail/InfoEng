# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 15:36:34 2017

@author: ksagilop
"""

import seaborn as sns
import matplotlib.pyplot as plt

'''
flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")
ax = sns.heatmap(flights)
'''

array = ([[91,  91, 0],
          [91,  91, 0],
          [91,  12, 0],
          [91,  91, 0],
          [91,  69, 0],
          [31,  18, 60],
          [90,  85, 1],
          [91,  21, 0],
          [91,  91, 0],
          [69,  69, 22]
          ])

y = ['CompanyName', 'ContactName', 'ContactTitle', 'Address',
     'City', 'Region', 'PostalCode', 'Country', 'Phone', 'Fax']

x = ['count', 'unique', 'missing']

ax = sns.heatmap(array, 
                 annot=True, 
                 yticklabels=y, 
                 xticklabels=x,
                 )

ax.set_title('Table Customers\n Row Value Descriptive Statistics')
ax.set_ylabel('Columns')
ax.set_xlabel('Feature')

'''
	CompanyName	ContactName	ContactTitle	Address	City	Region	PostalCode	Country	Phone	Fax
count	91	91	91	91	91	31	90	91	91	69
unique	91	91	12	91	69	18	85	21	91	69
'''

