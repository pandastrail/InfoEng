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
import os

''' ASSIGNMENTS '''
# Working .csv files iaw os
if os.name == 'posix':
    test = r'/home/hase/Documents/ZHAW/InfoEng/Lectures/Scripting/data/titanic3_test.csv'
    train = r'/home/hase/Documents/ZHAW/InfoEng/Lectures/Scripting/data/titanic3_train.csv'
elif os.name == 'windows':
    train = r'C:\ZHAW\lectures\scripting\data\titanic3_train.csv'
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

def describe(path):
    ''' Run basic parsing and calculations to get a basic
    description of the data. It assumes that there is a <survived> column. '''
    # CALCULATE
    data = read(path)                           # Read .csv file
    data = makeArray(data)                      # Create array
    passID = data[:,0]                          # Get passengers
    numPassengers = np.size(passID)             # Count passengers
    survived = data[:,2].astype(np.int)         # Get survived data
    numSurvived = np.sum(survived)              # Count survived 1s and 0s
    survivalQuota = numSurvived*100 / numPassengers
    genre = data[:,5]                           # Get genre data
    males = data[:,5] == 'male'                 # males True
    females = data[:,5] == 'female'             # females True
    numMales = np.size(data[males,5])           # Count males
    numMalesSurvived = np.sum(data[males,2].astype(np.float))  # Mask in survived
    numFemales = np.size(data[females,5])
    numFemalesSurvived = np.sum(data[females,2].astype(np.float))
    survivalMalesQuota = numMalesSurvived*100 / numMales
    survivalFemalesQuota = numFemalesSurvived*100 / numFemales
    #TODO Survival histogram by age
    
    # PRINT
    print('\nBasic calculations:')
    print('Passengers:', numPassengers)
    print(numMales, 'males,', numFemales, 'females')
    print('Survived:', numSurvived, '(', "%.2f" %survivalQuota, '%)') 
    print(int(numMalesSurvived), 'males',
      '(', "%.2f" %survivalMalesQuota, '%),',
      int(numFemalesSurvived), 'females',
      '(', "%.2f" %survivalFemalesQuota, '%)')
    
    # PLOT
    fig = plt.figure(figsize=(15,4))
    fig.suptitle('Data Description', fontsize=14, fontweight='bold')
    
    # Pie chart
    ax = fig.add_subplot(1,3,1)
    plt.pie([numPassengers - numSurvived, numSurvived],
            labels=['Not Survived', 'Survived'],
            autopct='%1.1f%%', #display percentages
            colors=plt.rcParams['axes.prop_cycle'].by_key()['color']) 
    ax.set_title('Survival Quota')
    
    ax = fig.add_subplot(1,3,2, facecolor='y')
    plt.pie([numMalesSurvived, numFemalesSurvived],
            labels=['Males', 'Females'],
            autopct='%1.1f%%') #display percentages
            #colors=plt.rcParams['axes.prop_cycle'].by_key()['color']) 
    ax.set_title('Survival Quota by Genre')
    # Show Figure
    plt.show()
    
''' EXECUTE '''
describe(train)
#TODO for test csv file submit key;value for probability by genre
#TODO make function to submit and retrieve score within this script
