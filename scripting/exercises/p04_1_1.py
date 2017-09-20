# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:53:25 2017

@author: ksagilop

P04 – Lists, Tuples & Dictionaries

1. Lists & Tuples
1.1 Battleship1
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

