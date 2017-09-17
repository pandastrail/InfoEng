#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 19:40:18 2017

@author: hase

Join the content of all text files in a folder into a new file
"""
# Modules
import os

# Path where the master file will be saved
folder = r'/home/hase/Documents/ZHAW/InfoEng/CASIE/Datenbanken/NamenUSA'
''' raw string: the r'..' string modifier causes the '..' string to be 
interpreted literally '''

# The join function of os.path constructs a pathname out 
# of one or more partial pathnames. 
# In this case, it simply concatenates strings
csv_filename = os.path.join(folder,'NamenUSAProStaat.csv');
csv_file = open(csv_filename,'w')  # Open (create) file to write

# Loop a directory to read file content and append
# to a master file
for filename in os.listdir(folder):  # os.listdir creates a list of files
    txt_filename = os.path.join(folder,filename)

    if txt_filename.endswith(".TXT"):  # only process files that end in .txt
        print('Processing:',filename)

        txt_file = open(txt_filename,'r') # Open file currently processed

        for l in txt_file.readlines():  # Readlines
            csv_file.write(l)           # Write lines to master file

        txt_file.close()

csv_file.close()

print("Done.")