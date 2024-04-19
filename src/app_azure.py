from flask import Flask, request, jsonify
import os
import requests
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Weather API', version='1.0.0')

# Compteur pour le nombre de requêtes traitées
request_counter = metrics.counter(
    'requests_by_type', 'Number of requests by type',
    labels={'endpoint': 'get_weather'}
)

# Définir la route racine qui réagira aux requêtes HTTP GET
@app.route('/')
def get_weather():
    # Récupérer les paramètres 'lat' (latitude) et 'lon' (longitude) de la requête HTTP
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')
    # Récupérer la clé API de la variable d'environnement OPENWEATHER_API_KEY
    api_key = os.getenv('OPENWEATHER_API_KEY')

    # Vérifier si tous les paramètres nécessaires sont présents
    if not all([latitude, longitude, api_key]):
        # Si un paramètre est manquant, retourner un message d'erreur et un code de statut HTTP 400 (Bad Request)
        return "Les variables d'environnement LATITUDE, LONGITUDE, et OPENWEATHER_API_KEY sont requises.", 400

    # Définir l'URL de base pour l'API OpenWeatherMap
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    # Préparer les paramètres de la requête à envoyer à l'API OpenWeatherMap
    params = {
        'lat': latitude,
        'lon': longitude,
        'appid': api_key,
        'units': 'metric'  # Définir les unités en métrique (Celsius)
    }
    # Faire une requête GET à l'API OpenWeatherMap avec les paramètres spécifiés
    response = requests.get(BASE_URL, params=params)
    
    # Vérifier si la réponse est réussie (code de statut HTTP 200)
    if response.status_code == 200:
        # Convertir la réponse JSON en un dictionnaire Python
        data = response.json()
        # Récupérer les informations météo de la réponse
        temperature = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        description = data['weather'][0]['description']
        country = data['sys']['country']
        city = data['name']
        # Retourner un JSON contenant les informations météo et un code de statut HTTP 200 (OK)
        return jsonify({
            "country": country,
            "city": city,
            "temperature": temperature,
            "temp_min": temp_min,
            "temp_max": temp_max,
            "description": description
        })
    else:
        # Si la requête échoue, retourner un JSON contenant le message d'erreur et le code de statut HTTP de la réponse
        return jsonify({"error": "Failed to fetch weather data"}), response.status_code

# Point d'entrée du script, cela permet de lancer le serveur uniquement si le script est exécuté directement
if __name__ == '__main__':
    # Démarrer l'application Flask sur le port 80 accessible de l'extérieur
    app.run(host='0.0.0.0', port=80)
