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

Optional:
- Create a program that simulates 10’000 runs of the “Guess the Number” game
(both players are now simulated by the computer) and compute the average
number of guesses needed to find the secrete number.
- Before you run the simulation, think about what average number you would expect.
"""
# Modules
import random

# Assignments
e = ('No pues, un numero entre 1 y 10: ')
i = list(range(1,11))       # Generate a list of valid integers

# Functions
def secret():
    '''Generate a random number between 1 and 10'''
    s = random.randint(1,10)
    print('secreto es: ', s)
    return s

def human():
    '''Get user guess for the secret number'''
    h = None                    # Initialize input
    while not (h in i):
        try: 
            h = int(input('Adivina un numero entre 1 y 10: '))
            if h not in i:              # Validate that input is within range
                print(e)                # Note that e is not an argument
            else:
                pass
        except ValueError:              # If input is not an integer
            print(e)
    return h

def play(h,s):
    while not (h == s):
        if h > s:
            print('Tu ', h, 'es MAYOR que el secreto')
            h = human()
        elif h < s:
            print('Tu ', h, 'es MENOR que el secreto')
            h = human()
        else:
            pass
    print('Correcto! Tu numero ', h, 'es igual a ', s)
    return

# Execute
s = secret()    
h = human()
play(h,s)