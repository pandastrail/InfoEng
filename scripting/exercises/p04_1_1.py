# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:53:25 2017

@author: ksagilop

P04 – Lists, Tuples & Dictionaries

1. Lists & Tuples
1.1 Battleship
Write a program that is a simplified, one-player version of the
classic board game “Battleship”. To start, use a 15x10 board,
save it as a list of lists and initialize a single boat of size 1x1 in
a random location on the board.

Let the player guess at most 10 times the location of the ship
(column number and row number). Make sure the guesses of
the player are inside the board.

Draw the board in the console after every guess of the player;
you could start by printing an ‘O’ everywhere (for ‘ocean’), 
then an ‘X’ for every wrong shot. 
The game can immediately end when the user hits the ship.

Hint:
- You can create a list with 10 elements (columns), each containing an "O", with
the expression row = ["O"] * 10
- You can append such a row to a list called board with the expression board-
.append(row)
"""

''' Modules '''
import random
from colorama import Fore, Back, Style    # Colored terminal output


''' Functions '''
def board(a,b):
    '''Create a board of '0's with size a x b'''
    # Create a row with <b> columns
    #row = ['0'] * b  # With this each row is a copy of the first one
    # With the following is the array directly created
    board_init = [['0'] * b for i in range(a)]
    # The following was to create the array with a loop
    # Append the row to a board with <a> rows
    #board_init = []
    #for i in range(a):
        #board_init.append(row)
    return board_init

''' Execute with user input '''
def start():
    ''' Ask for board size and initiate the game
    Generate a random location for a ship'''
    print('Let us play Battleship!')
    a = int(input('Board rows: '))
    b = int(input('Board columns: '))
    print('Game Board:')
    board_init = board(a,b)
    # Generate random int to establish a ship location
    a_loc = random.randint(0,(a-1)) # row
    b_loc = random.randint(0,(b-1)) # column
    # Locate the ship on the random index
    board_init[a_loc][b_loc] = 'X'
    return board_init, a, b

''' Inital board '''
board_init, a, b = start()
# Create header for columns
c = [[i] * 1 for i in range(b)]
print('  ', '\t', c)
for counter, row in enumerate(board_init, 1): # To create label for rows
    print(counter, '\t', row)
