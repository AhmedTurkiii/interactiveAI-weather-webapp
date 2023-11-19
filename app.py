# app.py

# Import necessary modules from Flask and the custom function for weather data
from flask import Flask, render_template, request
from main import get_weather_data

# Create a Flask app instance
app = Flask(__name__)

# Define a route for the home page which supports both GET and POST methods
@app.route('/', methods=['GET', 'POST'])
def home():
    # Initialize weather_data to None
    weather_data = None
    # Check if the request method is POST
    if request.method == 'POST':
        # Retrieve city name from the form data
        city = request.form['city']
        # Fetch weather data using the get_weather_data function
        weather_data = get_weather_data(city)
    # Render the weather.html template, passing the weather data
    return render_template('weather.html', weather=weather_data)

# Check if the script is executed directly (not imported) and then run the app
if __name__ == '__main__':
    app.run(debug=True)  # Running the app with debug mode enabled
