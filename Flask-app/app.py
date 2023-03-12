from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/weather/<city>')
def weather(city):
    # API endpoint for current weather
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=308924e01295471f74a0590473149807'

    # Retrieve the weather data
    response = requests.get(url)
    weather_data = response.json()

    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']

    return jsonify({
        'city': city,
        'temperature': temperature,
        'humidity': humidity,
        'description': description
    })

if __name__ == '__main__':
    app.run(debug=True)
