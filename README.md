# PROJET HBnB - Part 2


## Description du projet

Cette deuxième partie du projet HBnB consiste à donner vie à la conception technique réalisée dans la première partie.
L’objectif principal est de mettre en œuvre la logique métier et les endpoints d’API en utilisant Python, Flask, et Flask-RESTx.

Ce projet constitue la base du futur clone d’Airbnb, en introduisant les fonctionnalités fondamentales (sans authentification, ni autorisation à ce stade) :

* Création et gestion des utilisateurs, lieux, avis, et équipements.

* Implémentation de la logique métier sous forme de classes Python.

* Exposition d’une API RESTful claire, structurée et documentée.



## Architecture du projet :

part2/
│
├── app/
│   ├── __init__.py              → Initialise l’application Flask
│   │
│   ├── api/
│   │   └── v1/
│   │       ├── users.py         → Endpoints relatifs aux utilisateurs
│   │       ├── places.py        → Endpoints relatifs aux lieux
│   │       ├── reviews.py       → Endpoints relatifs aux avis
│   │       └── amenities.py     → Endpoints relatifs aux équipements
│   │
│   ├── models/
│   │   ├── modele_base.py       → Classe de base pour les modèles
│   │   ├── user.py              → Classe 'Utilisateur'
│   │   ├── place.py             → Classe 'Lieu'
│   │   ├── review.py            → Classe 'Avis'
│   │   └── amenity.py           → Classe 'Equipement'
│   │
│   ├── services/
│   │   ├── facade.py            → Classe 'HBnBFacade', interface unique vers la logique métier
│   │   └── __init__.py
│   │
│   └── persistence/
│       └── repository.py        → Définition du dépôt en mémoire (InMemoryRepository)
│
├── run.py                       → Point d’entrée de l’application
└── README.md                    → Documentation du projet



## Structure logique

1. Modèles

Les classes représentent les entités principales :

* Utilisateur
* Lieu
* Avis
* Equipement

Chaque modèle hérite de ModeleBase, qui gère :

* Un id unique
* La date de création
* La date de mise à jour


2. Dépôt en mémoire

Le fichier repository.py définit :

* Une interface abstraite Repository
* Une implémentation InMemoryRepository stockant les objets dans un dictionnaire Python.

**Cela permet de simuler une base de données sans en utiliser réellement.**


3. Façade

* facade.py implémente la classe HBnBFacade, jouant le rôle d’interface entre :

 - les API REST
 - la logique métier


 4. API (Presentation Layer)

Chaque fichier dans app/api/v1/ définit un namespace Flask-RESTx (par exemple : users, places, reviews, etc.).



## Endpoints disponibles : 

POST	-->  /api/v1/users/	      --> Créer un nouvel utilisateur
GET	  -->  /api/v1/users/	      --> Récupérer tous les utilisateurs
GET	  -->  /api/v1/users/<id>   -->	Récupérer un utilisateur par ID
PUT	  -->  /api/v1/users/<id>	  --> Mettre à jour un utilisateur

Chaque ressource (places, reviews, amenities) suit la même logique CRUD.

## Installation & Execution

* Créer un environnement virtuel :

python3 -m venv venv
source venv/bin/activate


* Installer les dépendances :

pip install flask flask-restx


* Lancer le serveur :

python3 run.py


* L’API est accessible à l’adresse :

http://127.0.0.1:5000/api/v1/



## Auteurs

* Grégory Sala

* Lucas Blancportier
