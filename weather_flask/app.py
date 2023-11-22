# app.py

# Import necessary modules from Flask and the custom function for weather data
from flask import Flask, render_template, request, send_file
from main import get_weather_data

# Create a Flask app instance
app = Flask(__name__)

# Define a route for the home page which supports both GET and POST methods
@app.route('/', methods=['GET', 'POST'])
def home():
    # Initialize weather_data to None
    weather_data = None
    # Variable to control form visibility
    show_form = True  
    # Check if the request method is POST
    if request.method == 'POST':
        # Retrieve city name from the form data
        city = request.form['city']
         # Hide the form when displaying weather data
        show_form = False 
        # Fetch weather data using the get_weather_data function
        weather_data = get_weather_data(city)
    # Render the weather.html template, passing the weather data
    return render_template('weather.html', weather=weather_data)

# Route for playing the audio file
@app.route('/play_audio')
def play_audio():
    filename = request.args.get('filename', 'default.mp3')
    audio_file_path = f"static/audio/{filename}"
    return send_file(audio_file_path, as_attachment=False)
    
# Check if the script is executed directly (not imported) and then run the app
if __name__ == '__main__':
    app.run(debug=True)  # Running the app with debug mode enabled
