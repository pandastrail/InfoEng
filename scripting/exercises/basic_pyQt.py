#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 10:01:12 2017

@author: hase

Build a basic Window with PyQt5
"""
# Modules
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction

# Classes
class Window(QMainWindow):
  '''Create class, inherit from PyQt5.QtWidgets.QMainWindow'''
  
  def __init__(self):
    '''Every time the <Window> object is called, everything below the 
     <__init__> method is executed.
    This function create the main window for the application and the 
    core components. It is also the container of the menu bar'''
    super(Window, self).__init__()  # Return parent object of this class
    self.setGeometry(500, 500, 500, 500)  # Starting points and size of window
    self.setWindowTitle('pyQt Basic Tutorial') # Title
    self.setWindowIcon(QIcon('logo.png'))  # Window icon
    
    extractAction = QAction('&Close', self)
    extractAction.setShortcut('Ctrl+Q')
    extractAction.setStatusTip('Close the application')
    extractAction.triggered.connect(self.close_app)
    
    extractAction2 = QAction('&Save', self)
    extractAction2.setShortcut('Ctrl+S')
    extractAction2.setStatusTip('Save File - does not do anything yet')
    
    extractAction3 = QAction('&Documentation', self)
    extractAction3.setShortcut('Ctrl+D')
    extractAction3.setStatusTip('Show Documentation')
    
    self.statusBar()
    mainMenu = self.menuBar()
    
    fileMenu = mainMenu.addMenu('&Datei')
    fileMenu.addAction(extractAction2)
    fileMenu.addAction(extractAction)
    
    helpMenu = mainMenu.addMenu('&Help')
    helpMenu.addAction(extractAction3)
    
    #self.show()  # This will be the same as Window.show() to show the window
    self.home()  # Call the method <home> defined below
  
  def home(self):
    '''Create what is placed at home. Here is also the toolbar placed.
    Toolbar can also be created at __init__'''
    # BUTTONS
    btn0 = QPushButton('quit', self) # Button to quit
    btn0.clicked.connect(QCoreApplication.instance().quit) # Define action
    btn0.resize(50,50)  # Resize manually
    btn0.move(100,200)  # Move from origin 0,0
    
    btn1 = QPushButton('close', self) # Button to close (redundant)
    btn1.clicked.connect(self.close_app) #action on click, calls method close_app
    btn1.resize(btn1.sizeHint())  # set to acceptable size automatic
    btn1.move(0,100)
    # END BUTTONS
    
    extractA = QAction(QIcon('logo.png'), 'Salir de la app', self)
    extractA.triggered.connect(self.close_app)
    
    self.toolBar = self.addToolBar('Add toolbar Salir')
    self.toolBar.addAction(extractA)
    
    self.show()  # Shows window
  
  def close_app(self):
    print('Si ahora no se apaga, se apaga luego') #print on the terminal
    sys.exit()

# Functions
def run():
  '''Runs the GUI and class defined'''
  app = QApplication(sys.argv)
  GUI = Window()  # Execute class Window
  sys.exit(app.exec_())

# Execute
run()