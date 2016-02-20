#! /usr/bin/python3
# quickWeather.py - Prints the weather for a location from command line

import json, requests, sys

# Compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
#location = ' '.join(sys.argv[1:]) USA format of location
location = sys.argv[1] # Rest of the world format of location

if location == 'Bratislava' or location == 'bratislava':
    cityId = 3060972
else:
    print('City not suported (yet :D). Sorry!')
    quit()

url = 'http://api.openweathermap.org/data/2.5/forecast?id=%s&APPID=aacbe57d2dfbe8ab5266c422eefc2519' % (cityId)
     # http://api.openweathermap.org/data/2.5/forecast?id=3060972&APPID=aacbe57d2dfbe8ab5266c422eefc2519
     # format on February 2016, may change in future
     
response = requests.get(url)
response.raise_for_status

# load json data intopython variable
weatherData = json.loads(response.text)

# Print weather description
w = weatherData['list']

print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
