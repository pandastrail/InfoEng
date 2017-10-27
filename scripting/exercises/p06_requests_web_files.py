# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:42:10 2017

@author: ksagilop

Use requests modules to retrieve info from website and download files

A nice tutorial:
https://gist.github.com/phillipsm/0ed98b2585f0ada5a769

TODO: List of books available
TODO: Merge this function with Gender Detection script
TODO: Analyze all books in url and provide statistics     
"""
# Modules
import requests, bs4

# Assignments
url = r'http://english-e-reader.net/findbook'
book_example = r'http://english-e-reader.net/download?link=macbeth-william-shakespeare&format=txt'

# Functions

def library(url):
    '''Get a list of available books to download from an specified <url>'''
    lib = requests.get(url)
    lib.raise_for_status()
    print(url)
    print('Text is', type(lib), 'of length', len(lib.text))
    libSoup = bs4.BeautifulSoup(lib.text, 'lxml')
    print(libSoup)
    print('Soup is', type(libSoup), 'of length', len(libSoup))
    elems = libSoup.select('table.table')
    print('Select is', type(elems), 'of length', len(elems))
    print(elems)
    for table_row in libSoup.select('table.table tr'):
        cells = table_row.findAll('td')
        if len(cells) > 0:
            books = cells[1]
            #print(books)
    return lib.text

def lease(book):
    '''Construct a list of available books to download'''
    res = requests.get(book)    # Requests a response from the url 'book'
    res.raise_for_status()      # Check call success
    print(type(res))
    print(len(res.text))
    print(res.text[:300])
    return res.text

# Execute
#lease(book_example)
#library(url)

lib = requests.get(url)
lib.raise_for_status()


