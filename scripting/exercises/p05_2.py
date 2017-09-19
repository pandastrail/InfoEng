#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:28:59 2017

@author: hase

2. Phone Book
Write a program that manages telephone numbers. It should be possible to
- add a new contact (name and number)
- remove a contact
- lookup a phone number for a given name
- save the contacts into a file
- load the contacts from a file
- save multiple numbers for the same person
- find people with typos
- find all that start with a letter
- save more data that belongs to that person, birthday, address, ...
- save the data into an excel sheet

My notes: write dict to txt and store, retrieve as needed
"""
""" Assignments """
# define dict for phone book (nested dict)
phone_book = {
        '077 123 45 67': {'name': 'Jon Doe', 'birth': '1980'},
        '078 321 90 80': {'name': 'Maria Schmid', 'birth': '1967'}
        }

""" a nested dict like
{'077 123 45 67': {'name': 'Jon Doe', 'birth': '1980'},
 '078 321 90 80': {'name': 'Maria Schmid', 'birth': '1967'}}
"""
menu_choice = 0

""" Functions """
def print_numbers(numbers):
    print(phone_book)
    pass
 
def add_number(numbers, name, number):
    #Todo
    pass
 
def lookup_number(numbers, name):
    #Todo
    pass
 
def remove_number(numbers, name):
    #Todo
    pass
 
def load_numbers(numbers, filename):
    #Todo
    pass
 
def save_numbers(numbers, filename):
    #Todo
    pass
# Prompt
def print_menu():
    '''A Menu or prompt to ask for action'''
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Lookup a Phone Number')
    print('5. Load numbers')
    print('6. Save numbers')
    print('7. Quit')
    print()
    return 

# Execute
print_menu()
# Make menu selection
while True:
    try:
        menu_choice = int(input("Type in a number (1-7): "))
    except ValueError:  # error handling for input not int
        print('Invalid input, please try again!')
        print_menu()
    if menu_choice == 1:
        print_numbers(phone_book)
    elif menu_choice == 2:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        add_number(phone_book, name, phone)
    elif menu_choice == 3:
        print("Remove Name and Number")
        name = input("Name: ")
        remove_number(phone_book, name)
    elif menu_choice == 4:
        print("Lookup Number")
        name = input("Name: ")
        print(lookup_number(phone_book, name))
    elif menu_choice == 5:
        filename = input("Filename to load: ")
        load_numbers(phone_book, filename)
    elif menu_choice == 6:
        filename = input("Filename to save: ")
        save_numbers(phone_book, filename)
    elif menu_choice == 7:
        break
    else:
        print('Invalid input, please try again!\n')
        print_menu()
 
print("Goodbye")
