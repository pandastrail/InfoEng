#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:37:25 2017

@author: hase

3. Gender Detection in Text
Write functions to automatically detect certain features of a text document 
(such as the gender of the author). For all functions, assume a text document 
as input in form of a single string, and create meaningful function- and 
parameter-names.

Background: The average native English speaker knows ca. one hundred thousand
words. According to research by psychologist James W. Pennebaker, however, 
the most revealing words in this impressive vocabulary are the ones we barely 
notice at all.

Gender-based language variations were among the first topics that Pennebaker 
studied with LIWC. Not surprisingly, he found that there are striking 
differences between the language usage of men and women. After analyzing 
thousands of blogs, essays, and other writing samples, he found that women use 
first-person singular pronouns like “I,” “me,” and “my” more frequently than men; 
according to his research, the average woman will use about 85,000 more pronouns 
per year than will the average man. Pennebaker attributes these findings to the 
tendency of women to be more self-aware than men, as has been documented by 
numerous psychological studies. He also found that women use more verbs and 
hedge phrases (such as “I think” and “I believe”), whereas men tend to use 
more numbers, nouns, and words per sentence. 

3.1 Count first-person singular pronouns
Write a function that counts the number of first-person singular pronouns 
(I, me, my) in a given text.
"""
# Modules
import os

# Assignments
folder = r'/home/hase/Downloads'

# Functions
def ebook():
    '''Ask for the input .txt file to analyze
    open, read it and assign its contents to a string'''
    file = input('.txt file to analyze: ')  # Ask for file name, incl.ext
    fileh = os.path.join(folder,file)       # Join folder path to file name 
    # Enconding is missing above!!!    
    with open(fileh, 'r') as f:             # Open file to read
        text = f.read()                     # Read entire file as one string
    print(fileh, 'is a ', type(text), 'with len', len(text))
    return text                             # return string

def pronouns(text):
    '''Counte first person singular pronouns, I, me, my'''
    countI = 0
    countme = 0
    countmy = 0
    pron = {}
    texto = text.split()                    # Create list of strings
    print('split to a', type(texto), 'with len', len(texto))
    for i in range(len(texto)):
        if 'I' == texto[i]:
            countI += 1
            pron['I'] = countI
        elif 'me' == texto[i]:
            countme += 1
            pron['me'] = countme
        elif 'my' == texto[i]:
            countmy += 1
            pron['my'] = countmy
        else: pass
    return pron

text = ebook()
pron = pronouns(text)
total_pron = sum(pron.values())
print('pron is a', type(pron), 'with len', len(pron))
print('pronouns dict', pron, 'for a total of', total_pron)
        
