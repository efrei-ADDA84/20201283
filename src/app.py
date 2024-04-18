from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_weather():
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')
    
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return jsonify({"error": "La clé API n'est pas définie."}), 500
    
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp'] - 273.15  # Conversion de Kelvin en degrés Celsius
        description = data['weather'][0]['description']
        country = data['sys']['country']
        city = data['name']
        temp_min = data['main']['temp_min'] - 273.15
        temp_max = data['main']['temp_max'] - 273.15
        return jsonify({
            "country": country,
            "city": city,
            "temperature": temperature,
            "temp_min": temp_min,
            "temp_max": temp_max,
            "description": description
        }), 200
    else:
        return jsonify({"error": "Erreur lors de la récupération des données météorologiques."}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
