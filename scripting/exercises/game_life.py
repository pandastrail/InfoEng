#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:01:35 2017

@author: hase
"""
# Modules
import os            # for clear screen
import copy          # for duplicating arrays
import random        # for random number generator
import colorama      # to address coordinates on screen

# Assignments
# definition of grid size
rows = 20
cols = 79
# initializations, e.g. board with random 0s and 1s
random.seed(); colorama.init()
generation = 0; empty = False

board = [[int(random.choice('01')) for x in
          range(cols)] for y in range(rows)]

os.system('cls' if os.name == 'nt' else 'clear')

while not empty:
    generation += 1
    new_board = copy.deepcopy(board)
    for y in range(rows):
        for x in range(cols):
#count the number of alive neighbours
#evaluate Conway's rules
#print updates directly to console
    board = copy.deepcopy(new_board)