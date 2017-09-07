# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 13:55:36 2017

@author: ksagilop
"""
#Modules
import urllib.parse, urllib.request, json

city_name = input("What city would you like to know about? ")

api_url = "http://wttr.in/%s" % urllib.parse.quote(city_name)

try:
 req = urllib.request.Request(api_url, headers = {"User-Agent": "curl"})
 response = urllib.request.urlopen(req)
 plaintext = response.read().decode("utf-8")
 print(plaintext[:plaintext.find("C") + 1])
except Exception as e:
 print("Couldn't connect to the weather service.", e)