# main.py
import requests

# Read the API key for the weather service from a file named 'api_key'
API_KEY = open('api_key_weatherAPI', 'r').read()



# Replace 'YOUR_API_KEY' with your actual Ipstack API key
api_key = '1ea250123d38d5d798f1756d72e248b1'

# Ipstack API endpoint
api_url = f'http://api.ipstack.com/check?access_key={api_key}'


def get_city():

    api_url = f'http://api.ipstack.com/check?access_key={api_key}'

    # Make a request to the Ipstack API
    response = requests.get(api_url)
    
    print(f"API Response: {response.text}")  # Add this line to print the entire response
    
    data = response.json()

    # Extract city information
    city = data.get('city', 'City not found')
    return city

# Function to fetch weather data for a given city
def get_weather_data(city):
    # Construct the URL for the weather API request
    url = f'http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=1&aqi=no&alerts=no'
    response = requests.get(url)
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response and return the data
        data = response.json()
        return data
    else:
        # In case of a non-200 response, print an error message
        print('Error fetching weather data')

