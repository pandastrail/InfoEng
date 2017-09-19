#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:23:51 2017

@author: hase

3. Transport at opendata.ch
Suppose the marketing department of your company would like to 
launch a campaign for a new product series. It would like to 
set up booths at train stations to reach as many people as possible. 
In order to prioritize where to set up booths, they would like to know...
- how many people can be reached
- between 4pm and 7pm on a weekday
- in six of the largest cities in Switzerland: 
    Zurich, Geneva, Basel, Lausanne, Bern and Winterthur.
    
The assumption is that the more trains depart, the more people will be there.
A web service at http://transport.opendata.ch provides information on 
the Swiss public transit system through a REST interface, 
e.g. for all timetable information of public transit in Switzerland. 

With a HTTP GET request to one of the three resources 
    /locations, 
    /connections or 
    /stationboard, a JSON response is returned containing
objects describing locations, stops, journeys and others. 
Detailed information is provided on the website.
"""
