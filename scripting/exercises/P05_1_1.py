# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

P05 – File I/O, Network I/O and JSON
1. File I/O
1.1 Change File Extension
Write a program that unifies the filename endings of MP3 songs
(.mp3 and .MP3) for all songs in a given folder to .mp3. 
Download the zip file containing the test data (these
are empty files, not actual songs) and extract it to a folder.

Hints:
- Make sure you import the module os: import os
- You can get a list of the files in a folder using
os.listdir(<path_to_folder>)
- You can rename a file using
os.rename(<old_filename>, <new_filename>)
- Research string methods (help(str)), e.g. replace(), endswith() or
join()
"""

# Modules
import os, shutil, random

# Assignments
work_path = r'H:\Downloads\temp'    # Working directory for exercise
clean_path = r'H:\Downloads\temp\mp3'    # Results directory for exercise

# Functions
# zip file containing examples was not found, create a folder
# with random .mp3 and .MP3 extensions
def extension():
    '''Assign file extension on a random basis'''
    e = random.randint(1,4)  # generate a random int from 1 to 4
    if e == 1:               # assign extension iaw random int   
        ext = '.mp3'
    elif e == 2:
        ext = '.Mp3'
    elif e == 3:
        ext = '.MP3'
    elif e == 4:
        ext = '.mP3'
    else:
        pass
    return ext

def songs(many):
    ''' Create blank .mp3 and .MP3 files with the number of
    files to be created as input for the function'''
    for i in range(many):       # list of int iaw input
        j = str(i)              # str instead int to add to path
        ext = extension()
        song = os.path.join(work_path, 'song' + j + ext)  # Path join
        f = open(song, 'x')     # create file
        print(song, 'created in ', work_path)
        f.close()               # close file and repeat loop
    return

# Execute first of program to create files if do not exist
#songs(35)

def clean():
    '''Change file extension to be .mp3 only'''
    count = 0                       # Initialize counters
    d = os.listdir(work_path)       # list of files in folder
    i = len(d)                      # number of files in folder
    for j in range(i):
        song = os.path.join(work_path, d[j])
        if d[j].endswith('.mp3'):
            print(song, 'NOT changed')
        if d[j].endswith('.Mp3'):
            mp3 = d[j].replace('Mp3', 'mp3')
            song_mp3 = os.path.join(clean_path, mp3)
            shutil.move(song, song_mp3)
            print(song, 'changed to ', song_mp3)
            count += 1
        if d[j].endswith('.MP3'):
            mp3 = d[j].replace('MP3', 'mp3')
            song_mp3 = os.path.join(clean_path, mp3)
            shutil.move(song, song_mp3)
            print(song, 'changed to ', song_mp3)
            count += 1
        if d[j].endswith('.mP3'):
            mp3 = d[j].replace('mP3', 'mp3')
            song_mp3 = os.path.join(clean_path, mp3)
            shutil.move(song, song_mp3)
            print(song, 'changed to ', song_mp3)
            count += 1
    return count

count = clean()
print(count, 'files were modified')
