#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:41:47 2017

@author: hase

4. Caesar cypher
Write a program that encrypts and decrypts a given message of lower-case text 
using a Ceasar cypher.

Background: In cryptography, a Caesar cypher, also known as Caesar's cypher, 
the shift cypher, Caesar's code or Caesar shift, is one of the simplest and 
most widely known encryption techniques. It is a type of substitution cipher 
in which each letter in the plaintext is replaced by a letter some fixed number 
of positions down the alphabet. For example, with a left shift of 3, D would be 
replaced by A, E would become B, and so on. The method is named after Julius 
Caesar, who used it in his private correspondence.

The encryption can also be represented using modular arithmetic by first 
transforming the letters into numbers, according to the scheme, 
a = 0, b = 1,..., z = 25.

The replacement remains the same throughout the message, so the cypher is 
classed as a type of monoalphabetic substitution, as opposed to polyalphabetic 
substitution. Hints:
- Think about what happens at the end of the alphabet.
- Only encrypt/decrypt the letters a-z
- Ensure all the characters in the message are in lower case. You can use the
python function lower(): lower_message = message.lower()
- You can represent each character as a number (called ordinal) using the ASCII
code of the character. It maps a to 97, b to 98, ..., z to 122.

Program to find the Unicode value of the given character:

print("The ASCII value of '" + c + "' is " + str(ord(c)))
print("The original character was " + chr(ord(c)))
"""
# Functions
def shift(msg, key):
    '''Get the unicode value of a string or the string for a value'''
    msg_mod = ''
    for c in msg:
        if ord(c) not in range(97,123):  # No ecryption for something other than lower case letter
            ec = c
            msg_mod += ec
        else:
            ec = chr((ord(c) - ord('a') + key) % 26 + ord('a'))
            msg_mod += ec
    return msg_mod

def encrypt(msg, key):
    '''Encrypt a message using Caesar cypher logic'''
    encrypt_msg = shift(msg, 3)
    return encrypt_msg

def decrypt(msg, key):
    '''Decrypt a message using Caesar cypher logic'''
    decrypt_msg = shift(msg, -3)
    return decrypt_msg

def user():
    '''Get input from user as a string'''
    msg = input("Enter your message: ")
    msg = msg.lower()         # Convert to lower-case
    return msg

# Execute
msg = user()
print('input: ', msg)
encrypt_msg = encrypt(msg, 3)
print('encrypted:', encrypt_msg)
decrypt_msg = decrypt(encrypt_msg, -3)
print('decrypted:', decrypt_msg)


