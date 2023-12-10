# app.py

# Import necessary modules from Flask and the custom function for weather data
from flask import Flask, render_template, request, send_file
from main import get_weather_data,get_city
from openai import OpenAI


# Opening and reading the API KEY
OPENAI_API_KEY = open('api_key_openai', 'r').read()

# Create a Flask app instance
app = Flask(__name__)

# Define a route for the home page which supports both GET and POST methods
@app.route('/', methods=['GET', 'POST'])
def home():
     # Render the form
   
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():

    if 'cityInput' in request.form:
            # Get city from form data
            city = request.form['city']
    elif 'autoDetection' in request.form:
            # Get city from form data or use auto-detection logic
            city = get_city() 
    #request.form['city']
    # Fetch weather data
    weather_data = get_weather_data(city)
    current_condition = weather_data['current']['condition']['text'].lower()
    current_temperature = weather_data['current']['temp_f']
    client = OpenAI(api_key=OPENAI_API_KEY)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a program that gives clothing recommendations based on weather conditions. Your response is only the clothing and nothing else. Provide shoes, bottoms, shirt/sweater. Output example: Rain boots, pants, sweater. Only give me one of each."},
            {"role": "user", "content": f"It is currently {current_condition} and the temperature is {current_temperature}°F. Give me clothing recommendations"}
        ]
    )
    clothing_recommendations = str(completion.choices[0].message.content)
    clothing_recommendations = clothing_recommendations.replace('Shoes:', '').replace('Bottoms:', '').replace('Shirt/Sweater:', '')

    # Render the results page with weather data
    return render_template('results.html', weather=weather_data, clothing=clothing_recommendations)

# Route for playing the audio file
@app.route('/play_audio')
def play_audio():
    filename = request.args.get('filename', 'default.mp3')
    audio_file_path = f"static/audio/{filename}"
    return send_file(audio_file_path, as_attachment=False)
    
# Check if the script is executed directly (not imported) and then run the app
if __name__ == '__main__':
    app.run(debug=True)  # Running the app with debug mode enabled
