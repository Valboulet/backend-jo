# JO-billetterie-backend

Il s'agit de la partie back-end de l'application web de billetterie des Jeux Olympiques. C'est un projet django et postgresql

## Pré-requis

Pour l'application web :

- [Python 3.12.4](https://www.python.org/downloads/)
- [PostgreSQL 16.4](https://www.postgresql.org/download/)
- [Docker](https://docs.docker.com/desktop/install/mac-install/)

## Installation en local et lancement

1. Cloner le repository depuis la branche 'main'

2. Après avoir cloné ce repo,  trouver le fichier docker-compose.yml et vérifier les configurations spécifiques, comme les variables d’environnement. 
Si nécessaire, crée un fichier .env contenant les variables requises ou modifie les chemins si des volumes locaux doivent être montés.

3.  Ensuite, aller dans le dossier dossier backend-jo/backend, puis éxécuter la commande `docker-compose up -d --build`

4. Une fois les conteneurs démarrés, accéder à l'adresse locale [http://localhost:8000](http://localhost:8000)


## Plus d'infos

Pour aller plus loin, consulter la [documentation technique](https://lively-quality-3f6.notion.site/Bloc-3-Studi-Examen-10b0cf88bc12807482ebf115edf7458e) du projet.
