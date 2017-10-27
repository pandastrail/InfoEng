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
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import (QApplication, 
                            QWidget, 
                            QMainWindow, 
                            QPushButton,
                            QAction,
                            QMessageBox,
                            QCheckBox,
                            QProgressBar,
                            QComboBox, QLabel, QStyleFactory,
                            QFontDialog,
                            QToolTip)

# Initializations

# Classes

class Window(QMainWindow):  
    '''Create class, inherit from PyQt5.QtWidgets.QMainWindow'''
  
    def __init__(self):
        '''Every time the <Window> object is called, everything below the 
        <__init__> method is executed.
        This function create the main window for the application and the 
        core components. It is also the container of the menu bar'''
        super(Window, self).__init__()  # Return parent object of this class
        # setGeometry(x,y,x,y)
        self.setGeometry(700, 200, 500, 500)  # Starting points and size of window
        self.setWindowTitle('pyQt Basic Tutorial') # Title
        self.setWindowIcon(QIcon('logo.png'))  # Window icon
        QApplication.setStyle(QStyleFactory.create('Fusion')) #App Style
    
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
        
        # Place another toolbar
        anotherTool = QAction('Another', self)
        self.toolBar = self.addToolBar('Another')
        self.toolBar.addAction(anotherTool)
        
        # Add toolbar for font selection
        fontChoice = QAction('Font', self)
        fontChoice.triggered.connect(self.font_choice)
        self.toolBar = self.addToolBar('Font')
        self.toolBar.addAction(fontChoice)
    
        #self.show()  # This will be the same as Window.show() to show the window
        self.home()  # Call the method <home> defined below
        
    def font_choice(self):
        '''When selected it changes font of Qlabel'''
        font, valid = QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)
            print('font is', font)
  
    def home(self):
        '''Create what is placed at home. Here is also the toolbar placed.
        Toolbar can also be created at __init__
        Here is also a checkbox defined; and a progress bar'''
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
        
        checkBox = QCheckBox('Check a box', self)
        # checkBox.toggle()  # if you want to be checked in in the begin
        checkBox.move(0, 50) # Move the checkbox to a different corrdinate
        checkBox.stateChanged.connect(self.checking)
        
        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn2 = QPushButton('Descargar', self)
        self.btn2.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn2.move(200, 120)
        self.btn2.clicked.connect(self.download)
        
        texto = 'a string passed to header'
        self.header_example = QLabel(texto, self) #Qlabel has a max char?
        self.header_example.move(25,320)
        
        print(self.style().objectName())
        print(QStyleFactory.keys())
        self.styleChoice = QLabel('Default', self)
        comboBox = QComboBox(self)
        comboBox.addItem('Windows')
        comboBox.addItem('WindowsXP')
        comboBox.addItem('WindowsVista')
        comboBox.addItem('Fusion')

        comboBox.move(25, 280)
        self.styleChoice.move(25, 150)
        comboBox.activated[str].connect(self.style_choice)

        self.show()  # Shows window
    
    def style_choice(self, text):
        print(text)
        self.styleChoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))
        print('changed to', self.style().objectName())
    
    def download(self):
        self.completed = 0
        print('Progress bar is at', self.completed)
        
        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)
        print('Progress bar is at', self.completed)         
        
    def checking(self, state):
        if state == Qt.Checked:
            print('Checkbox is checked')
        else:
            print('Checkbox is unchecked')
  
    def close_app(self):
        '''Pop up to ask if sure to quit or not.
        The last variable in QMessageBox is the default selection!'''
        choice = QMessageBox.question(self, 'Message',
                                     "Tas seguro que te vas?",
                                     QMessageBox.Yes | QMessageBox.No, 
                                     QMessageBox.No)
        if choice == QMessageBox.Yes:
            print('Salir de la App')
            sys.exit()
        else: 
            pass

# Functions
def run():
    '''Runs the GUI and class defined'''
    app = QApplication(sys.argv)
    GUI = Window()  # Execute class Window
    sys.exit(app.exec_())

# Execute
run()