'''
P07 – Regex

1. Credit Card check with regular expressions

Suppose you have been hired by MeisterCard to write a function which 
checks if a given credit card number is valid. Your function 
check(card_number) should take a string card_number as input.

- First, if the string does not follow the format 
"#### #### #### ####", where each # is a digit, it should return False.
- Then, if the sum of the digits is divisible by 10 (a "checksum" method), 
then the procedure should return True, otherwise it should return False.
- For example, if card_number is the string "9384 3495 3297 0123" then
although the format is correct, the digit’s sum is 72 so you should return False.

Employ regular expressions wherever suitable.
'''

''' MODULES '''
import re

''' FUNCTIONS '''
''' Using string split
def number_format(s):
    number_parts = s.split(' ')
    print('string splitted is', number_parts)
    if len(number_parts) != 4:
        return False
    for part in number_parts:
        if len(part) != 4:
            return False
        elif not part.isdigit():
            return False
    print('Correct format.')
    return True
'''

def number_format(s):
    '''Use regex to check for the correct card number format'''
    match = re.search(r'^\d{4} \d{4} \d{4} \d{4}$', card_number)
    if match:
        print('Using regex, Found:', match.group())
        return True
    else:
        print('Using regex, Not found')
        return False

def check(s):
    '''Once the format has been checked, do a checksum and divisible'''
    if number_format(s):  # If return of number_format(s) is True
        '''Above show a function call with an if-statement'''
        digit_sum = 0
        print('input to check is', s)
        for digit in s:
            #print('digit in s is', digit)
            if digit != ' ':   # If different from a blank space
                digit_sum += int(digit) # Sum the digits
        if digit_sum % 10 == 0:  # Checksum divisable by 10
            print('Correct checksum:', digit_sum % 10)
            return True
        else:
            print('Incorrect checksum:', digit_sum % 10)
    return False

''' EXECUTE '''
# Correct format and checksum
card_number = '9384 3495 3297 0121'
print('Card number is', card_number)
print(check(card_number))
# Correct format and incorrect checksum
card_number = "9384 3495 3297 0123"
print(check(card_number))
# Incorrect format
card_number = "9384 1495 3297 0125"
print(check(card_number))



