# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:33:35 2017

@author: gilop

Survival Probability
First try, basic functions, understanding the problem
"""
''' MODULES '''
import os
import time
import csv
import numpy as np
import matplotlib.pyplot as plt
from selenium import webdriver

''' ASSIGNMENTS '''
# Working .csv files iaw os
if os.name == 'posix':
    test = r'/home/hase/Documents/ZHAW/InfoEng/Lectures/Scripting/data/titanic3_test.csv'
    train = r'/home/hase/Documents/ZHAW/InfoEng/Lectures/Scripting/data/titanic3_train.csv'
    deliver = r'/home/hase/Documents/ZHAW/InfoEng/Lectures/Scripting/data/submit/titanic_deliver_'
elif os.name == 'nt':
    train = r'C:\ZHAW\lectures\scripting\data\titanic3_train.csv'
    test = r'C:\ZHAW\lectures\scripting\data\titanic3_test.csv'
    deliver = r'C:\ZHAW\lectures\scripting\data\submit\titanic_deliver_'
# initialize a list to store the content of the .csv file
data = []

# Place to submit the predictions
url_submit = 'https://openwhisk.ng.bluemix.net/api/v1/web/ZHAW%20ISPROT_ISPROT17/default/titanic.html' 

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
    description of the data. 
    It assumes that there is a <survived> column '''
    # Get data
    data = read(path)                           # Read .csv file
    data = makeArray(data)                      # Create array
    
    # CALCULATE
    passID = data[:,0]                          # Get passengers
    numPassengers = np.size(passID)             # Count passengers
    survived = data[:,2].astype(np.int)         # Get survived data
    maskSurvived = data[:,2] == '1'
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
    ages = data[:,6] != ''                      # Mask ages, exclude blanks
    numAges = np.size(data[ages,6])             # Count records with age data
    Ages = data[ages,6].astype(np.float)
    numAgesSurvived = np.sum(data[ages,2].astype(np.float))
    maskAgesSurvived = data[ages,2] == '1'
    agesSurvived = Ages[maskAgesSurvived]
    
    # PRINT
    print('\nBasic calculations:')
    print('Passengers:', numPassengers)
    print(numMales, 'males,', numFemales, 'females')
    print('Survived:', numSurvived, '(', "%.2f" %survivalQuota, '%)') 
    print(int(numMalesSurvived), 'males',
      '(', "%.2f" %survivalMalesQuota, '%),',
      int(numFemalesSurvived), 'females',
      '(', "%.2f" %survivalFemalesQuota, '%)')
    print(numAges, 'records have an age data')
    
    # PLOT
    fig = plt.figure(figsize=(15,4))
    fig.suptitle('Data Description', fontsize=14, fontweight='bold')
    
    # Pie chart Survival Quota
    ax = fig.add_subplot(2,2,1)
    plt.pie([numPassengers - numSurvived, numSurvived],
            labels=['Not Survived', 'Survived'],
            autopct='%1.1f%%', #display percentages
            colors=plt.rcParams['axes.prop_cycle'].by_key()['color']) 
    ax.set_title('Survival Quota for all Passengers')
    
    # Pie chart Survival Quota by Genre
    ax = fig.add_subplot(2,2,2)
    plt.pie([numMalesSurvived, numFemalesSurvived],
            labels=['Males', 'Females'],
            autopct='%1.1f%%') #display percentages
    ax.set_title('Survival Quota by Genre')
    
    # Histogram Age Dsitribution
    ax = fig.add_subplot(2,2,3)
    plt.hist(Ages, bins=80)
    ax.set_title('Age Distribution')
    
    # Histogram Survival Quota by Age
    ax = fig.add_subplot(2,2,4)
    plt.hist(agesSurvived, bins=80)
    ax.set_title('Survival Quota by Age')
    
    # Show Figure
    plt.show()

def predict(path, output):
    ''' Using the test file provided, create a ke;value .csv file
    with a prediction who will survive.
    It assumes that there is NO <survived> column '''
    data = read(path)                           # Read .csv file
    data = makeArray(data)                      # Create array
    count = 0
    output = output + time.strftime('%Y%m%d%H%M%S') + '.csv'
    
    # ID-1 Survival Probaility based on gender
    with open(output, 'w') as f:
        csv_out = csv.writer(f, delimiter=';')
        csv_out.writerow(['key', 'value'])
        # initialize a list to subtmit the results to leaderboard
        leader = ''
        leader += 'key' + ';value\n'
        for row in data:
            if row[4] == 'female':
                csv_out.writerow([row[0], '1'])
                leader += row[0] + ';1\n'
                count += 1
            elif row[4] == 'male':
                csv_out.writerow([row[0], '0'])
                leader += row[0] + ';0\n'
                count += 1
        print(output, 'created with', count, 'entries')
    #print(leader)
    #print(type(leader))
    
    ask = input('Submit test results to leaderboard? [y/n] ')
    if ask == 'y':
        submit(url_submit, leader)
    else:
        print('Ok, bye')

def submit(url, long_str):
    ''' Submit the key;value csv file to the corresponding leaderboard
    Asjust the name and id entered and retrieve the leaderboard status. '''
    
    driver = webdriver.Chrome()
    driver.get(url)
    
    # Define name + id to submit
    head = 'team_nr_' + time.strftime('%Y%m%d%H%M%S')
    # Find text box to write name + id to submit
    name_id = driver.find_element_by_name('submission') 
    name_id.send_keys(head)
    
    # Find text box to paste csv key;value
    paste_csv = driver.find_element_by_name('csv') 
    paste_csv.clear()  # Clear to be able to write from list
    # Paste key;value, needs to be a string and not a list
    paste_csv.send_keys(long_str)
    # Submit button
    submit_btn = driver.find_element_by_xpath('/html/body/form/input[2]')
    submit_btn.submit()
    
    # it appears that if there are print statements here 
    # then the chrome application is closed

''' EXECUTE '''
#describe(train)
predict(test, deliver)
