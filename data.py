# Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name
import requests
from datetime import datetime
# api_key = 'Enter API Key'
api_key = 'b4b936c974fe4fcaa7235112230711'

city = input('Enter city name: ')
url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=1&aqi=no&alerts=no'

# url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q=seaside&days=1&aqi=no&alerts=no'
print(url)
response = requests.get(url)
if response.status_code == 200:
    data = response.json()

    temp = int(data['current']['temp_f'])
    desc = data['current']['condition']['text']
    first_forecast_day = data['forecast']['forecastday'][0]
    low_temp = first_forecast_day['day']['mintemp_f']
    high_temp = first_forecast_day['day']['maxtemp_f']
    sunrise = first_forecast_day['astro']['sunrise']
    sunset = first_forecast_day['astro']['sunset']
    print(f'Current Temperature: {temp}°F')
    print(f'Description: {desc}')
    print(f'low: {low_temp}°F, high: {high_temp}°F')
    print(f'Sunrise: {sunrise}')
    print(f'Sunset: {sunset}')
    # print(f'next time: {next_time}')
    # print(f'next hour: {next_hour}°F')
    # print(f'Weather at {next_time} is {next_hour}°F')
    for i in range(0, 24):
        condition = first_forecast_day['hour'][i]['condition']["text"]
        next_time = first_forecast_day['hour'][i]['time']
        parsed_datetime = datetime.strptime(next_time, "%Y-%m-%d %H:%M")
        next_time = parsed_datetime.strftime("%I:%M %p")
        next_hour = int(first_forecast_day['hour'][i]['temp_f'])
        rain_chance = int(first_forecast_day['hour'][i]['chance_of_rain'])
        print(f'Weather at {next_time}: {next_hour}°F')
        if rain_chance > 0:
            if "rain" in condition:
                break
            print(f'Description {condition} With {rain_chance}% chance of rain\n')
        else:
            print(f'Description {condition}\n')

    # Split the military time into hours and minutes
else:
    print('Error fetching weather data')
