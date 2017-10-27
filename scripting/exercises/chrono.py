# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:17:44 2017

@author: ksagilop

A very siple stopwatch to get the effort to be registered on an effort log
"""
# Modules
import time
import webbrowser

# Assignments
trail = 'http://kuntani.ch/!pandastrail/doku.php?id=forms:neweffort'
i = 0                                   # Counter
laps = {}                               # Dict with interval times
hrs = []                                # Accumulate the differences

# Functions

def form():
    print('You have worked', "%.2f" % total, 'hrs! or', 
          "%.2f" % total_min, 'min\n')
    k = input('Launch pandastrail form? (y/n) ')
    if k is 'y':
        webbrowser.open(trail)
        input('Form opened. Enter to close!')
    else:
        pass

def pausa(i):
    '''Calculate the lap time when a pause is requested'''
    pause = time.time()
    lap_feed = time.strftime('%H:%M:%S')      # Get current time as string
    print('\nLap', i, 'time is:', lap_feed)     # Feedback
    i += 1
    laps[i] = pause
    hrs.append((laps[i] - laps[i-1])/3600)
    laps.clear()
    restart(i)
    return i

def restart(i):
    '''Restart the device'''
    input('Enter to restart')
    restart = time.time()
    restart_feed = time.strftime('%H:%M:%S')      
    print('\nRestart', i, 'time is:', restart_feed)     
    i += 1
    laps[i] = restart
    ask(i)
    return i
 
def ask(i):
    '''Pause or stop the device and act accordingly'''
    btn = input('...and counting. Enter to stop! or (p)pause ')
    if btn is 'p':
        pausa(i)
    else:
        stop(i)
    return i
 
def stop(i):
    '''Get the last time of the device after user selects stop'''
    stop = time.time()
    stop_feed = time.strftime('%H:%M:%S')
    print('\nStop time is', stop_feed, '\n')
    i += 1
    laps[i] = stop
    hrs.append((laps[i] - laps[i-1])/3600)
    laps.clear()
    return i

# Execute
input('''Grüezi, so you wanna know how much time you will put, 
      Write Keyword and Enter to go! 
      Tag: ''')                         # User input
start = time.time()                     # Time as float in sec
i += 1                                  # Initialize counter
laps[i] = start                         # Append to dict
start_feed = time.strftime('%H:%M:%S')  # Get current time as string
print('\nStart time is:', start_feed)     # Feedback
ask(i)
#print(laps)
total = sum(hrs)
total_min = total*60
form()