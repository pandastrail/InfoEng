# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 17:11:33 2017

@author: ksagilop

5 Parrot
Echo the input

Create a program that behaves like a well-trained parrot: 
it just repeats any input.

Again, the code itself will be quite simple (more so if you consider that for this
automated parrot it is ok to do the trick only once and then quit). 

Use the time therefore to think for yourself of what steps this program can 
be composed and what python constructs you already know to realize them. 

Ignore all possible programs that need
more Python knowledge than you yourself (currently) have under command.
"""


# Validate that n is an positive integer number and less than five
# Give feedback if criteria is not met
# Then gather input n-times, every character is possible (string)
# Echo each input
# At the end construct a random phrase with the input
# And search for it on google, and bring the results page
# Then ask if parrot will play again

# Constants
e = 'Invalid input, try again'

# Functions
def valid(n):
    i = list(range(1,6)) # Generate a list of integers
    if n not in i:       # Validate that integer is within range
        print(e)
    else:
        print('good')
    return n

# Input
try:                     # Validate if input is an integer
    n = int(input('Hi, how many entries you want to make (from 1 to 5)? '))
    valid(n)
except:
    print(e)



