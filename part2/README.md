# PROJET HBnB - Part 2


## Description du projet

Cette deuxième partie du projet HBnB consiste à donner vie à la conception technique réalisée dans la première partie.
L’objectif principal est de mettre en œuvre la logique métier et les endpoints d’API en utilisant Python, Flask, et Flask-RESTx.

Ce projet constitue la base du futur clone d’Airbnb, en introduisant les fonctionnalités fondamentales (sans authentification, ni autorisation à ce stade) :

* Création et gestion des utilisateurs, lieux, avis, et équipements.

* Implémentation de la logique métier sous forme de classes Python.

* Exposition d’une API RESTful claire, structurée et documentée.



## Architecture du projet :

<img width="527" height="469" alt="Capture d’écran 2025-10-19 à 00 22 58" src="https://github.com/user-attachments/assets/1cce1ab0-2184-49fb-8f08-e3d909d99914" />



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

POST	-->  /api/v1/users/	     --> Créer un nouvel utilisateur
GET	 -->  /api/v1/users/	     --> Récupérer tous les utilisateurs
GET	 -->  /api/v1/users/<id>  -->	Récupérer un utilisateur par ID
PUT	 -->  /api/v1/users/<id>	 --> Mettre à jour un utilisateur

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



TESTS :

Créer utilisateur : 

<img width="466" height="692" alt="Créer un nouvel utilisateur" src="https://github.com/user-attachments/assets/f417b0fb-6ecf-4e3c-a565-f84c79e83b24" />

Récupérer une liste d'utilisateurs :

<img width="476" height="585" alt="Récupérer liste utilisateur " src="https://github.com/user-attachments/assets/ed621eca-0c08-405a-a2c2-8b0aaa327a1e" />


Créer un nouvel équipement :

<img width="471" height="719" alt="Créer un nouvel équipement " src="https://github.com/user-attachments/assets/79dd5049-77f8-48a3-bacb-9316a20c4d85" />

Récupérer une liste d'équipement :

<img width="489" height="628" alt="Récupérer une liste d'equipement " src="https://github.com/user-attachments/assets/230485fd-3394-4ad0-9293-2859a179124a" />



## Auteurs

* Grégory Sala

* Lucas Blancportier
