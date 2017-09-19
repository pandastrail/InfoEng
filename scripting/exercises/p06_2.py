#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:28:59 2017

@author: hase

2. Credit Card Number Check
Suppose you have been hired by MeisterCard to write a function 
which checks if a given credit card number is valid. 
Your function check(card_number) should take a string card_number as input.

- First, if the string does not follow the format "#### #### #### ####", where
each # is a digit, it should return False.
- Then, if the sum of the digits is divisible by 10 (a "checksum" method), 
then the procedure should return True, otherwise it should return False.

For example, if card_number is the string "9384 3495 3297 0123" then although
the format is correct, the digit’s sum is 72 so you should return False.

Hints:
- You can split a string at a specific character using the function split().
parts = my_string.split('a')
- You can test if a string contains only digits with the function isdigit().
only_digits = my_string.isdigit()
"""
# Modules
import numpy as np

# Functions
def invalid():
    ''' Feedback to user after an invaid input'''
    print('Invalid number, please try again!')
    
def card():
    ''' Get user input with card number'''
    card_num = input('Card number, #### #### #### ####? ')
    if len(card_num) == 19:
        sanitized = card_num.split(' ')
        s = len(sanitized)
        if s == 4:
            i = range(s)
            for i in sanitized:
                if sanitized[i].isdigit():
                    print('Valid number!')
            else: invalid()
        else: invalid()
    else: invalid()
    return card_num

card()    
                         

