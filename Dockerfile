# Utilisation d'une image Python officielle comme image parente
FROM python:3.8-slim

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers nécessaires dans le conteneur
COPY src/ .

# Installation des dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Commande par défaut à exécuter lorsque le conteneur démarre
CMD ["python", "weather_wrapper.py"]
