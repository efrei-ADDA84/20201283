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

## Contexte : 

Dans ce TP, nous avons utilisé python et la bibliothèque Flask pour créer une API qui à partir d'une longitude et latitude renvoie les données météo associées grâce à l'API Openweather. L'objectif était ensuite de s'initier à la création d'un workflow github action qui permet d'executer des tâches à chaque comit sur le projet.

## Etapes réalisées : 

- Codé l'API avec la bibliothèque Flask
- Créer le build.yml pour configurer le workflow
- Créer les variables secretes
- Créer l'image docker
- Après avoir testé l'API à travers l'image docker, j'ai ajouté hadolint qui m'a permis de détécter des éléments deprecated dans mon code


# Rapport TP3 : 

## Liens et commande : 

Azure : https://portal.azure.com/#@efrei.net/resource/subscriptions/765266c6-9a23-4638-af32-dd1e32613047/resourceGroups/ADDA84-CTP/providers/Microsoft.ContainerInstance/containerGroups/20201283/overview
Accéder à l'image docker dans le conteneur registry : curl "http://devops-20201283.francesouth.azurecontainer.io/?lat=48.8566&lon=2.3522"
résutat : {"city":"Paris","country":"FR","description":"overcast clouds","temp_max":11.11,"temp_min":8.84,"temperature":9.82}

## Contexte : 

Dans ce TP, nous avons créer un workflow permettant de réaliser automatiquement plusieurs actions sur azure. Allant du build du containeur à son déploiement sur azure. L'objectif est donc d'automatiser ces tâches qui pourrait prendre du temps à chaque push du code.

## Etapes réalisés : 

- Changer le port de connexion
- Modifier le build.yml pour configurer les workflows (build and push et deploy)
- Créer les variables secrètes pour la connexion à azure
- Push son code pour tester les workflows
- Faire appel au containeur registry

## Difficultées

Réussir à configurer le buil.yml car il faut trouver les bonnes fonctions misent à dispositions. Problème plus général connaître les régions qui serait disponible pour le déploiement, heureusement ici vous aviez donné les solutions. 

