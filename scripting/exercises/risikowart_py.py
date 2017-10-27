# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:10:28 2017

DE Edition

TODO Create Classes as needed
TODO Do not repeat yourself

"""
''' print library '''
assess_ask = 'Wollen Sie eine Risikobewertung durchführen? [j/n] '


''' Every function represents a screen on the GUI '''
def startScreen():
    ''' Gets the basics of the device being processed '''
    # TODO For the first 3 inputs need a list or dropdown and select
    # This should be pre-defined, if not an exception is always possible
    device_label = input('Gerätebezeichnung: ')
    device_mfg = input('Hersteller: ')
    device_type = input('Typenbezeichnung: ')
    # A part of this variable is also somehow pre-defined
    # Nonetheless, a free-text should be here possible
    # This will play a certain bias on the overall evaluation
    device_aim = input('Verwendungszweck, kurze Beschreibung: ')
    # From here should jump to next function/screen
    # And insert record in database, from this and all other screens

def mfgDefaults():
    ''' Set what are the manufacturing defaults for the service '''
    # Error handling
    err_interval = 'Bitte eine Ganzzahl zwischen 1 und 60 eingeben!'
    # STK is trasnlated as safety-related check
    # The input should be prettier on the GUI
    # This info can/could also be pre-defined, no? Service Manual?
    mfg_check = input('Schreibt der Hersteller eine STK vor? [j/n] ')
    if mfg_check == 'j':
        # Input should be int and between 1 and 60 months
        mfg_check_interval = None           # Initialize to loop as needed
        while not mfg_check_interval:
            try:
                mfg_check_interval = int(input('alle wie viele Monate? '))
                # On the GUI need to advise for valid values
                # Or provide radiobuttons and alternative if not included
                if not mfg_check_interval > 0:
                    print(err_interval)
                    mfg_check_interval = None 
                elif not mfg_check_interval <= 60:
                    print(err_interval)
                    mfg_check_interval = None 
            except:
                print(err_interval)
    else:
        pass
    # From here should jump to next function/screen

def reqAppF():
    ''' Requirements IAW EN 62363, Appendix F 
    Anforderungen gemäss EN 62353, Anhang F '''
    # A list of checkboxes?
    # Help functions? Defaults?
    # if one of the points here defined is selected a check interval
    # longer than 24 months is not recommended
    appF_selected = input('Something selected from EN 62363? [y/n] ')
    if appF_selected == 'y':
        reqAppFtrue()
    else:
        reqAppFfalse()

def reqAppFtrue():
    ''' If one of the point iaw EN 62363 was selected, 
    the following info and option should appear '''
    print('Die Prüffrist sollte... nicht > 24 Monate sein!')
    # Move on if the risk assesment is needed
    assess = input(assess_ask)
    if assess == 'j':
        severity()
    else:
        # Record the device as evaluated, NO risk assessment performed
        # with all data, and jumpt to dashboard
        pass

def reqAppFfalse():
    ''' If none of the criteria iaw EN 62363 was selected '''
    print('Keins der Kriterien gemäss EN 62353 (Anhang F) trifft zu.')
    assess = input(assess_ask)
    if assess == 'j':
        severity()
    else:
        pass
        # Record the device as evaluated, NO risk assessment performed
        # with all data, and jumpt to dashboard

def severity():
    ''' Measure of damages '''  
    print('Schadensausmass bei Fehlfunktion oder Geräteausfall')
    
    
''' TESTING '''
#startScreen()
#mfgDefaults()
reqAppF()