# JO-billetterie-backend

Il s'agit de la partie back-end de l'application web de billetterie des Jeux Olympiques. C'est un projet django.

## Pré-requis

Pour l'application web :

- [Python 3.12.4](https://www.python.org/downloads/)
- [MySQL 8.1.0](https://dev.mysql.com/doc/relnotes/mysql/8.1/en/)

## Installation en local

1.  Après avoir cloné ce repo, aller dans le dossier backend-jo : `cd backend-jo`, puis créer l'environnement virtuel `python -m venv venv`

2.  Activer l'environnement virtuel juste créé :

- sur MacOs/Linux : `source venv/bin/activate`
- sur Windows : `venv\Scripts\activate`

3. Installer Django et les dépendances nécessaires : `pip install -r requirements.txt`

4. Créer une base de données MySQL

5. Dans backend-jo/backend/backend/settings.py, remplacer les valeurs :

- SECRET_KEY : par une secret key générée ici : [https://djecrety.ir/](https://djecrety.ir/)
- DATABASE_NAME : par le nom de votre base de données MySQL
- DATABASE_USER : par le nom d'utilisateur de votre BDD
- DATABASE_PASS : par votre mot de passe

## Lancement

1. Retourner dans le premier dossier backend : `cd backend`

2. Éxécuter la commande `python manage.py runserver` pour accéder au serveur local du projet django à l'adresse : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Pour aller plus loin, consulter la [documentation technique]() du projet.
