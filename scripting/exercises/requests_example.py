# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:02:13 2017

@author: ksagilop
"""
import requests
from bs4 import BeautifulSoup

url_to_scrape = r'http://english-e-reader.net/findbook'
r = requests.get(url_to_scrape)
s = BeautifulSoup(r.text, 'lxml')

t = s.find_all('tr')
print(t)

