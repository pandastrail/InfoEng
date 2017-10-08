#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 22:02:10 2017

@author: hase

More SQL-Python examples
"""
# Library
import mysql.connector
import matplotlib.pyplot as plt

# Connection with DB
cnx = mysql.connector.connect(user = 'root', 
                              password = 'root',
                              host = '127.0.0.1', 
                              database = 'NamenUSA'
                              )
cursor = cnx.cursor()

print(cnx)
print(cursor)

# Query
"""
cursor.execute('''SELECT
                   Name, Year, SUM(Births)
               FROM 
                   NamenUSAProStaat
               GROUP BY
                   Name, Year
               HAVING
                   SUM(Births) > 90000;'''
                )
"""

cursor.execute('''
SELECT
	Name, Year, SUM(Births)
FROM
	NamenUSAProStaat
WHERE
    Name = 'Michael'
GROUP BY
	Year
ORDER BY
	SUM(Births) DESC;'''
    )

q = cursor.fetchall()
print('queryResult is a ', type(q), 'with length', len(q))
#print(q)
y = []
b = []
for i in q:
    print(i)
    y.append(i[1])
    #print(i[2])
    b.append(i[2])

plt.plot(y,b, 'bs')
plt.ylabel('Births')
plt.xlabel('Year')
plt.show()