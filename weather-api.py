'''
Create a weather data analyzer using an API (fetch weather data 
and display basic stats).
'''

# Importing the requests and json modules
import requests
import json
from os import getenv


# Fetching data from an API [Weather API] #

# API Key
api_key = getenv('WEATHER_API_KEY')

# Endpoint
endpoint = "current.json"

# Base URI to access the API
base_uri = f"http://api.weatherapi.com/v1/{endpoint}"

# print(base_uri) # Debugging

# Creating the params obj/dict
params = {
    'key': api_key,
    'q': 'London',
    'days': 1
}

# Fetching the data from the API
try:
    response = requests.get(base_uri, params=params)  # Sending a GET request to the API
    if response.status_code == 200:  # Status code 200 indicates a successful response
        data = response.json()  # Parsing the JSON data / .json.dumps() -> converts to JSON format


        # Displaying the data
        print(data)  # Data is a dictionary

        print('\n-----------------------------------\n')

        # Displaying the first element of the data
        print(data['current'])

        print('\n-----------------------------------\n')

        # Displaying the temperature
        print('Temperature:', data['current']['temp_c'])

        print('\n-----------------------------------\n')

        # Displaying the humidity
        print('Humidity:', data['current']['humidity'])

        print('\n-----------------------------------\n')

        # Displaying the wind speed
        print('Wind Speed:', data['current']['wind_kph'])

    else:
        print('Error:', response.status_code, response.text)  # Displaying the error message

except Exception as e:
    print('Error:', e)