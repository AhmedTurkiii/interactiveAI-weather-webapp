# main.py
import requests
from datetime import datetime

# Read the API key for the weather service from a file named 'api_key'
API_KEY = open('api_key_weatherAPI', 'r').read()

# Function to fetch weather data for a given city
def get_weather_data(city):
    # Construct the URL for the weather API request
    url = f'http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=1&aqi=no&alerts=no'
    # Make an HTTP GET request to the weather API
    response = requests.get(url)
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response and return the data
        data = response.json()
        return data
    else:
        # In case of a non-200 response, print an error message
        print('Error fetching weather data')
        # Optionally, return None or handle the error as needed
        # return None
