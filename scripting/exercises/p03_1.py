#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 10:40:32 2017

@author: hase

1.2 Rock Paper Scissors

Write a program for the rock-paper-scissors game where one person is simulated 
by the computer and the other is the actual user.

Rock-paper-scissors is usually played by two people, where players 
simultaneously form one of three shapes with an outstretched hand. 

The rules are
- the "rock" beats scissors
- the "scissors" beat paper and
- the "paper" beats rock;
- if both players throw the same shape, the game is tied.

Hints:
- Just simulating one round of the game is enough; optionally, you can of course
enhance your implementation to play until one party has, say, 3 wins.
- Generate a random number to simulate the computers choice.
- To generate a random number use:
import random
random_number = random.randint(lower_bound, upper_bound)
"""
# Modules
import random

# Assignments
i = 0       # Robot win counter
j = 0       # Human win counter

# Functions
def compu():
    ''' Get a random number between 1 and 3'''
    r = random.randint(1,3)
    if r == 1:
        robot = "piedra"
    if r == 2:
        robot = "papel"
    if r == 3:
        robot = "tijera"
    else:
        pass
    print('Compu :', robot)
    return r

def user():
    '''Get user input, an option between 1 and 3'''
    u = None       # Initialize user input
    while not (u == 1 or u == 2 or u == 3):
        human = input('piedra, papel o tijera? ')
        print('Tu    :', human)
        if human == 'piedra':
            u = 1
        elif human == 'papel':
            u = 2
        elif human == 'tijera':
            u = 3
        else:
            print('What??? ')
    return u

def play(u,r,i,j):
    '''Compute the result of a single game'''
    if u == r:
        print('\nEmpate!, otra vez...')
    if u == 1 and r == 2:   # piedra pierde con papel
        i += 1
        print('                            Compu ', i, ':', j, ' Tu')
    if u == 1 and r == 3:   # piedra le gana a tijera
        j += 1
        print('                            Compu ', i, ':', j, ' Tu')
    if u == 2 and r == 1:   # papel le gana a piedra
        j += 1
        print('                            Compu ', i, ':', j, ' Tu')
    if u == 2 and r == 3:   # papel pierde con tijera
        i += 1
        print('                            Compu ', i, ':', j, ' Tu')
    if u == 3 and r == 1:   # tijera pierde con piedra
        i += 1
        print('                            Compu ', i, ':', j, ' Tu')
    if u == 3 and r == 2:   # tijera le gana al papel
        j += 1
        print('                            Compu ', i, ':', j, ' Tu')
    return i, j
    
# Execute
print('Buenas, vamos a ver, a tres juegos, listos, sal!')
# A while not (condition) to loop for 3 games
while not (i == 3 or j == 3):
    u = user()
    r = compu()
    game = play(u,r,i,j)
    i = game[0]
    j = game[1]
    #print('i: ', i)
    #print('j:', j)
    
# Finalize after condition is met
if i == 3:
    print('\nLa Compu gana! ... uuu')
elif j == 3:
    print('\nTu ganas amig(a)ouu!!!')

