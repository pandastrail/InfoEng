#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:43:50 2017

@author: hase

Simple example using mysql-connector
"""
# Library
import mysql.connector

# Connection with DB
cnx = mysql.connector.connect(user = 'root', 
                              password = 'root',
                              host = '127.0.0.1', 
                              database = 'ClassicModels'
                              )
cursor = cnx.cursor()

print(cnx)
print(cursor)

# Query
cursor.execute('''SELECT 
                       *
                  FROM
                      offices;'''
                )

q = cursor.fetchall()
print('queryResult is a ', type(q), 'with length', len(q))
#print(q)

for i in q:
    print(i[1])


            
                            

