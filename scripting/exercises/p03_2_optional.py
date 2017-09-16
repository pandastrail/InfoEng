#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:40:07 2017

@author: hase
2.1 Guess the Number
In this exercise you’ll create a little game. Here is how to play:
- Your program will pick a secret number between 1 and 10.
- The user guesses what number it is.
- If the user’s guess is too high or too low, the program will give the user a hint.

Hint:
- Loop as long as the secret number is not found.

Optional (BINARY SEARCH):
- Create a program that simulates 10’000 runs of the “Guess the Number” game
(both players are now simulated by the computer) and compute the average
number of guesses needed to find the secrete number.
- Before you run the simulation, think about what average number you would expect.
"""
# Modules
import random
import bisect
import timeit
import numpy as np

# Assignments
start = 1
stop = 1000000
j = 0
i = list(range(start,stop + 1))       # Generate a list of valid integers
timed = []

# Functions
def secret():
    '''Generate a random number between 1 and 10'''
    s = random.randint(start,stop)
    #print('secret number: ', s)
    return s

def compu(s):
    '''Robot must guess the secret number'''
    found = bisect.bisect(i, s, lo=0, hi=len(i))
    #print('secret number is: ', found)
    return found

# Execute
while not (j == 10000):
    inicio = timeit.default_timer()
    s = secret()
    compu(s)
    fin = timeit.default_timer()
    t = fin - inicio
    timed.append(t)
    j += 1
    #print('It took ', timed, 'sec to compute') 

time_avg = np.mean(timed)
time_sum = np.sum(timed)
print('Avg. time to compute each bisect: ', time_avg)
print('Total time to compute: ', time_sum)