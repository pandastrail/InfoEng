#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 21:09:18 2017

@author: hase

Use selenium to submit a result to the leaderboard

"""
from selenium import webdriver

url = 'https://openwhisk.ng.bluemix.net/api/v1/web/ZHAW%20ISPROT_ISPROT17/default/titanic.html'

driver = webdriver.Chrome()
driver.get(url)

try:
    name_id = driver.find_element_by_name('submission') 
    print('Found <%s> element with that class name!' % (name_id.tag_name))
except:
    print('not found')

name_id.send_keys('submission_file_plus_time')

try:
    paste_csv = driver.find_element_by_name('csv') 
    print('Found <%s> element with that class name!' % (name_id.tag_name))
except:
    print('not found')

paste_csv.clear()

paste_csv.send_keys('Key;Value\n')
paste_csv.send_keys('12345;1\n')
paste_csv.send_keys('678;0\n')

# Submit button Selector:
# body > form > input[type="submit"]:nth-child(7)
# Xpath:
# /html/body/form/input[2]
try:
    submit = driver.find_element_by_xpath('/html/body/form/input[2]')
    print('Found <%s> element with that class name!' % (name_id.tag_name))
except:
    print('not found')

    