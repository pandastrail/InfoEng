# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:33:35 2017

@author: gilop

Survival Probability
First try, basic functions, understanding the problem
"""
''' MODULES '''
import csv
import numpy as np
import matplotlib.pyplot as plt

''' ASSIGNMENTS '''
# Working .csv file
path = r'C:\ZHAW\lectures\scripting\data\titanic3_train.csv'
# initialize a list to store the content of the .csv file
data = []

''' FUNCTIONS '''
def read(path):
    ''' Read the .csv file into a python object.
    Create a numpy array from a list '''
    print('\nReading .csv file...')
    with open(path, 'r') as f:
        csv_raw = csv.reader(f, delimiter=';')
        print(csv_raw, 'created')
        print('Creating list...')
        for row in csv_raw:
            data.append(row)
        print(type(data), 'of len', len(data), 'created')
    return data

def makeArray(aList):
    ''' Convert a list object into a numpy array.
    Convert str objects into int or float objects as needed.
    First row is assumed to be the header'''
    print('\nCreating numpy array...')
    anArray = np.array(aList)
    print(type(anArray), 'of shape (row,col):', anArray.shape, 'created')
    print('Array columns:')
    rows, columns = anArray.shape
    for col in range(columns):
        print('#', col, anArray[0,col])
    # Remove header
    anArray = np.delete(anArray, 0, 0)
    #print(anArray)
    return anArray

''' EXECUTE '''
# Read .csv file
data = read(path)
# Create array
data = makeArray(data)
# Check array
#print('\n', data)
# Count the number of passengers
passID = data[:,0]
numPassengers = np.size(passID)
# How many passengers survived
survived = data[:,2].astype(np.float)
numSurvived = np.sum(survived)
survivalQuota = numSurvived*100 / numPassengers
# Hoy many males and females are and survival quota
males = data[:,5] == 'male'
females = data[:,5] == 'female'
numMales = np.size(data[males,5])
numMalesSurvived = np.sum(data[males,2].astype(np.float))
numFemales = np.size(data[females,5])
numFemalesSurvived = np.sum(data[females,2].astype(np.float))
survivalMalesQuota = numMalesSurvived*100 / numMales
survivalFemalesQuota = numFemalesSurvived*100 / numFemales
# OUTPUT
print('\nBasic calculations:')
print('Passengers:', numPassengers)
print(numMales, 'males,', numFemales, 'females')
print('Survived:', int(numSurvived), '(', "%.2f" %survivalQuota, '%)') 
print(int(numMalesSurvived), 'males',
      '(', "%.2f" %survivalMalesQuota, '%),',
      int(numFemalesSurvived), 'females',
      '(', "%.2f" %survivalFemalesQuota, '%)'
      )

