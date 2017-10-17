# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:50:53 2017

@author: ksagilop

P07 Regex

2. Regular expression for URLs

Based on the script v07_regex_contact_data.py discussed in class:

-Design a regular expression to extract a valid URL and add it to the script
- Instead of first occurrence, extract all occurrences of phone numbers, 
emails and URLs
- Refactor your code to using functions for extracting all phone numbers, email
addresses and URLs
- Test your code on email-footer.txt

Hint:look up re.findall()
See also https://docs.python.org/2/library/re.html#match-objects
"""
''' MODULES '''
import re

''' ASSIGNMENTS '''
filename = r'/home/hase/Documents/ZHAW/InfoEng/Lectures/Scripting/code/v07_email-footer.txt'

''' FUNCTIONS '''
def read_file(filename):
    ''' Load text file to analyze '''
    try:
      f = open(filename, 'r')
    except IOError as detail:
      print("Cannot open file "+filename, detail)
      exit()
    else:
      with f:  # This is the same as with open(filename, 'r') as f:
        text = f.read()
      return text

def phone(text):
    ''' Find phone numbers, either international or local format '''
    phones = re.findall(r'\+\d{2} \d{2} \d{3} \d{4}', text) # International
    phones.append(re.findall(r'0\d{2} \d{3} \d{4}', text)) # Local
    if phones: 
      #print(phones, 'of type', type(phones), 'len', len(phones))
      return True, phones
    else:
      return False

def email(text):
    ''' Find email addresses '''
    #FIXME email_match = re.search(r'[\w.-]+@[\w.-]+', text)
    pass


''' EXECUTE '''
text = read_file(filename)
# Print the text extracted
print(text)
# Find phone numbers
print('Phones found:')
print(phone(text))