"""

import os
import sys
import requests

def get_weather(latitude, longitude):
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        print("Erreur: La clé API n'est pas définie.")
        return None
    
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
        return temperature, description, country, city, temp_min, temp_max
    else:
        return None

if __name__ == "__main__":
    latitude = os.getenv("latitude")
    longitude = os.getenv("longitude")
    
    if not latitude or not longitude:
        print("Erreur: Les coordonnées de latitude et longitude ne sont pas définies.")
        sys.exit(1)
    
    weather_data = get_weather(latitude, longitude)
    if weather_data:
        temperature, description, country, city, temp_min, temp_max = weather_data
        print(f"Pays : {country}")
        print(f"Ville : {city}")
        print(f"Température actuelle : {temperature:.2f} °C")
        print(f"Température minimale : {temp_min:.2f} °C")
        print(f"Température maximale : {temp_max:.2f} °C")
        print(f"Description : {description}")
    else:
        print("Erreur lors de la récupération des données météorologiques.")
"""