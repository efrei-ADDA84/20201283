# Rapport des TP

# Rapport TP1

## Liens et commande : 

Docker hub : https://hub.docker.com/r/juleslogerot/meteo2julio
Commande d'exécution : docker run -e OPENWEATHER_API_KEY=votre api key -e latitude=latitude -e longitude=longitude meteo2julio

## Etapes réalisées :

- Création d'un environnement virtuel afin de télécharger les librairies nécessaires 
- Crétaion d'une clé API sur le site d'openweather
- Ecriture du fichier weather_wrapper.py permettant de se connecter à l'api en récupérant les informations souhaitées. Ici la température, une brève description, le pays, la ville, la température max, la température min.
- Configuration des variables d'environnement, ici la clé api
- Création du dockerfile : utile lors de la création de l'image pour charger le contenue dans son environnement et se configurer avec le requiremment puis lancement du fichier weather_wrapper.py.
- Création de l'image docker avec dockerbuild
- Pour exécuter le code passer en paramètre d'environnement la clé api, ainsi que la latitude et la longitude du lieu souhité
- Push de l'image docker avec docker push


# Rapport TP2

## Liens et commande : 

Docker hub : https://hub.docker.com/r/juleslogerot/meteoapi2
Commande d'exécution : docker run -d --name meteoapi2 -p 8080:8080 --env OPENWEATHER_API_KEY=votre api key meteoapi2
Accéder à l'api sur un autre terminal : curl "http://localhost:8080/?lat=5.902785&lon=102.754175"

## Etapes réalisées : 

- Codé l'API avec la bibliothèque Flask
- Créer le build.yml pour configurer le workflow
- Créer le variables secretes
- Créer l'image docker
- Après avoir testé l'API à travers l'image docker, j'ai ajouté hadolint qui m'a permis de détécter des éléments deprecated dans mon code