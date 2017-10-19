'''
 Looks up connections using JSON api at transport.opendata.ch
 Provide a city name and a start time
 connections within the start time plus one hour are provided.

 NOTE: JSON api returns approximately 40 connections,
        at big stations this will not cover an entire hour.
        In this case additional requests are issued to fill one hour.
'''
import sys
import urllib.request, urllib.parse, urllib.error
import json
from datetime import datetime, timedelta, date

# API Website
api_url = "http://transport.opendata.ch/v1/stationboard"

# Initialize datetime objects to validate the input
start = 0
stop = 0

def dictURL(city_name, start):
    ''' Prepare http get variables as dictionary '''
    get_values = {}
    get_values.clear()
    get_values = {}
    get_values["station"] = city_name
    get_values["datetime"] = start.strftime('%Y-%m-%d %H:%M')#start time
    get_values["transportations[]"] = 's_sn_r'# just get the s-bahn
    # More than one type of train
    #transportations = [ 'ice_tgv_rj', 'ec_ic', 'ir', 're_d', 's_sn_r']
    return get_values

def human():
    ''' Get user input ''' 
    city_name = input("Looking up trains. Which city? ")
    start_time = input("What time? Type like 22:30 ") 
    #TODO Start time could also be now!
    start, stop = validTime(start_time)
    return city_name, start_time, start, stop

def validTime(start_time):
    ''' Validate format of datetime objects ''' 
    try:
        start = datetime.combine(date.today(),
                         datetime.strptime(start_time,'%H:%M').time())
        stop = start + timedelta(hours=1,minutes=1)
        return start, stop
    except Exception as detail_start:
        print(detail_start)
        start = 0
        stop = 0
        return start, stop

def getTrains(city_name, start_time, start, stop):
    ''' Get Train connections for selected city and start time '''
    # Initialize dictionary to parse the URL
    get_values = dictURL(city_name, start)
    try:
        got_one_hour = False
        num_requests = 0
        count = 0
    
        print('Connections leaving from',city_name)
        print('between',start.strftime('%H:%M'),"and",stop.strftime('%H:%M'))

        while not got_one_hour:
            url_values = urllib.parse.urlencode(get_values)
            # if you chose more than one train type
            #for item in transportations:
            #    url_values = url_values + '&transportations[]='+item

            full_url = api_url + "?" + url_values

            #debug only
            #print full_url

            response = urllib.request.urlopen(full_url)
            json_tree = json.loads(response.read().decode("utf-8"))

            if 'stationboard' in json_tree:
                num_requests +=1
                
                all_journeys = json_tree['stationboard']
            
                for journey in all_journeys:
                    dep_time = datetime.strptime(journey['stop']['departure'][:16],'%Y-%m-%dT%H:%M')
                    if dep_time < stop:
                        count +=1
                        print('  ',journey['name'],'-to-', journey['to'], ' at', dep_time.strftime('%H:%M'))
                    else:
                        got_one_hour = True
                        break
                get_values["datetime"] = (dep_time + timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M')
            else:
                print('HTTP response seems to be empty')
                break
        print('found',count,'connections using',num_requests,'requests')

    except Exception as detail_api:
        print("Couldn't connect to the transport api.", detail_api)

# Ask for input until datetime objects are validated
while start == 0:
    city_name = None
    start_time = None
    city_name, start_time, start, stop = human()
# Get train connections
getTrains(city_name, start_time, start, stop)
