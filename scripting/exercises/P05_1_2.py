# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 14:44:57 2017

@author: ksagilop

1.2 Recursive Directory Tree
Implement a program that asks for a directory and 
prints all the files in that directory recursively
as a tree.

Hints:
- Use the os.listdir() and os.path.isdir() functions
"""
# Modules
import os

def user():
    '''Get path to be read in the form <H:\Downloads\temp>'''
    path = input('Directory path? ')
    return path

# Using listdir is not clear how to do the recursive
def tree(path):
    '''Construct the directory tree iaw the path provided'''
    s = '\\'                # construct a \ literaly by \\
    print(path + s)
    items = os.listdir(path)
    for i in range(len(items)):
        item = os.path.join(path, items[i])
        if os.path.isdir(item):
            print('|--', items[i] + s)
        else: print('|--', items[i])
    return
        
path = user()
#tree(path)

# Another way to get folder, subfolder and files is with os.walk
for dirs, subs, files in os.walk(path):
    print(dirs)
    print(subs)
    print(files)