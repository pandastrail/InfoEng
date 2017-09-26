# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:42:10 2017

@author: ksagilop

Use urllib modules to retrieve info from website and download files

TODO: List of books available
TODO: Merge this function with Gender Detection script
TODO: Analyze all books in url and provide statistics     
"""
# Modules
import requests

# Assignments
url = r'http://english-e-reader.net/findbook'
book_example = r'http://english-e-reader.net/download?link=macbeth-william-shakespeare&format=txt'

# Functions
def library(book):
    '''Construct a list of available books to download'''
    res = requests.get(book)   # Requests a response from the url 'book'
    print(type(res))
    print(len(res.text))
    print(res.text[:300])
    return res.text

library(book_example)

