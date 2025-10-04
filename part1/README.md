# Documentation Technique HBnB — Diagrammes et Explications Détaillés

## Introduction

Cette documentation présente l’architecture conceptuelle et technique du projet **HBnB**, une application inspirée d’Airbnb permettant aux utilisateurs de créer, consulter et évaluer des lieux d’hébergement. Ce document regroupe tous les diagrammes UML nécessaires à la compréhension du système :

* Le **diagramme de paquetage**, pour visualiser la structure globale du projet.
* Le **diagramme de classes**, qui détaille les entités de la logique métier.
* Les **diagrammes de séquence**, qui illustrent les interactions entre les différentes couches lors d’appels API clés.

L’objectif est d’avoir une vision claire et cohérente afin de servir de support à la phase d’implémentation.

---

## 1. Diagramme de paquetage — Vue d’ensemble de l’architecture

### Objectif du diagramme

Le **diagramme de paquetage** présente la structure globale du système HBnB. Il permet de visualiser comment le projet est divisé en sous-parties logiques, chacune ayant une responsabilité bien définie.

### Description

Le système est organisé selon une architecture en **trois couches principales** :

1. **Couche Présentation** :

   * Gère la communication avec les utilisateurs et les requêtes HTTP.
   * Fournit les terminaisons API pour les opérations telles que la création d’un utilisateur, l’ajout d’un lieu ou la soumission d’un avis.

2. **Couche Logique Métier** :

   * Contient les modèles et les règles de gestion (classes `Utilisateur`, `Lieu`, `Avis`, `LieuEquipement`, etc.).
   * Applique les validations et la cohérence des données avant leur enregistrement.

3. **Couche Persistance (Base de Données)** :

   * Responsable du stockage, de la récupération et de la suppression des données.
   * Contient les interactions SQL avec la base.

<img width="291" height="702" alt="Diagramme de paquetage HBNB" src="https://github.com/user-attachments/assets/23c63879-a196-4f54-bbd9-c6c6d56ef1db" />

### But

Ce diagramme montre **comment les différentes couches interagissent entre elles** tout en restant indépendantes. Ainsi, le code est plus clair, réutilisable et facile à maintenir.

---

## 2. Diagramme de classes — Logique métier

### Objectif du diagramme

Le **diagramme de classes** décrit la structure interne de la couche logique métier. Il montre les entités principales de l’application, leurs attributs, leurs méthodes et les relations entre elles.

### Description des classes principales

#### Classe `Utilisateur`

* **Rôle** : représente les utilisateurs inscrits sur l’application.
* **Attributs principaux** : `id`, `nom`, `email`, `mot_de_passe`.
* **Méthodes** :

  * `creationProfil()` — crée un nouvel utilisateur.
  * `modificationProfil()` — met à jour les informations du profil.
  * `suppressionProfil()` — supprime le compte utilisateur.

#### Classe `Lieu`

* **Rôle** : représente un ou des logements disponibles sur la plateforme.
* **Attributs principaux** : `id`, `titre`, `description`, `prix`, `latitude`, `longitude`, `nbr_chambres`, `nbr_max_voyageurs`.
* **Méthodes** : `ajouterLieu()`, `modifierLieu()`, `supprimerLieu()`.

#### Classe `LieuEquipement`

* **Rôle** : gère les équipements disponibles dans un lieu (ex : Wi-Fi, climatisation, frigo, parking, etc.).
* **Attributs principaux** : `id_lieu`, `id_equipement`.
* **Relation** : relie plusieurs équipements à un même lieu.

#### Classe `Avis`

* **Rôle** : représente les avis laissés par les utilisateurs sur les lieux.
* **Attributs principaux** : `id`, `note`, `commentaire`, `id_utilisateur`, `id_lieu`.
* **Méthodes** : `ajouterAvis()`, `modifierAvis()`, `supprimerAvis()`.

#### Classe `ModeleBase`

* **Rôle** : classe abstraite servant de modèle parent pour les autres entités.
* **Contient** : les attributs et méthodes communs (`id`, `date_creation`, `date_modification`).

### Relations entre les classes

* `Utilisateur` peut **créer plusieurs** `Lieu`.
* `Lieu` peut **avoir plusieurs** `Avis`.
* `Lieu` peut **posséder plusieurs** `Equipements` via `LieuEquipement`.
* `Avis` est lié à **un seul** `Utilisateur` et **un seul** `Lieu`.

<img width="556" height="707" alt="Diagramme de classes HBNB" src="https://github.com/user-attachments/assets/b05c3d48-429c-4a77-9ca5-02c452453fa4" />

### But

Ce diagramme aide à comprendre **la structure des données** et **la logique métier** sans entrer dans le code. Il sert de plan et garantit la cohérence des relations dans la base de données.

---

## 3. Diagrammes de séquence — Interactions API

### Objectif général

Les **diagrammes de séquence** illustrent le **flux d’interactions entre les couches** du système lors des appels API. Chaque diagramme correspond à un cas d’usage concret.

---

### 3.1 Diagramme de séquence — Utilisateur (Inscription, Modification, Suppression)

#### Objectif

Montrer comment un utilisateur interagit avec l’API pour créer, modifier ou supprimer son profil.

#### Fonctionnement

1. L’utilisateur envoie une requête (POST, PUT, DELETE) à l’API.
2. L’API vérifie la validité des champs.
3. La logique métier applique les règles (mot de passe valide, email unique, etc.).
4. Les données sont enregistrées, modifiées ou supprimées dans la base.
5. L’API retourne un message clair (succès ou erreur).

#### Codes d’erreur gérés

* **201 Created** : profil créé avec succès.
* **400 Bad Request** : champs invalides.
* **404 Not Found** : utilisateur inexistant.
* **500 Internal Server Error** : erreur serveur.

<img width="913" height="595" alt="Diagramme de séquence Utilisateur HBNB" src="https://github.com/user-attachments/assets/7c2c61f2-d2d6-4273-8822-e33a674f3774" />

---

### 3.2 Diagramme de séquence — Lieu (Création d’un lieu)

#### Objectif

Représenter le processus complet de création d’un lieu par un utilisateur.

#### Fonctionnement

1. L’utilisateur soumet un formulaire de création.
2. L’API vérifie les données (prix, coordonnées, description…).
3. La logique métier valide les règles.
4. Les données sont sauvegardées dans la base.
5. L’API renvoie un message de confirmation ou d’erreur.

#### Codes d’erreur gérés

* **201 Created** : lieu ajouté avec succès.
* **400 Bad Request** : champs invalides.
* **409 Conflict** : lieu déjà existant.
* **500 Internal Server Error** : erreur d’enregistrement.

<img width="1045" height="704" alt="Diagramme de séquence Lieu HBNB" src="https://github.com/user-attachments/assets/f8bdebee-1399-4031-9407-337eeddde1a6" />

---

### 3.3 Diagramme de séquence — Lieu & Équipement

#### Objectif

Montrer comment l’application recherche et renvoie une liste de lieux selon certains critères (prix, localisation, équipements…).

#### Fonctionnement

1. L’utilisateur effectue une requête GET avec des filtres.
2. L’API valide les critères.
3. La logique métier transmet la demande à la base.
4. La base renvoie soit une liste, soit un résultat vide.

#### Codes d’erreur gérés

* **200 OK** : liste retournée ou vide.
* **400 Bad Request** : critères invalides.

<img width="815" height="571" alt="Diagramme de séquence LieuEquipement" src="https://github.com/user-attachments/assets/d772aa38-50ac-45c9-bbbe-2cacf599ee2a" />

---

### 3.4 Diagramme de séquence — Avis

#### Objectif

Illustrer la création d’un avis par un utilisateur sur un lieu donné.

#### Fonctionnement

1. L’utilisateur envoie un avis avec note et commentaire.
2. L’API vérifie la validité et la complétude des champs.
3. La logique métier vérifie que l’utilisateur et le lieu existent.
4. Si tout est conforme, l’avis est enregistré.

#### Codes d’erreur gérés

* **201 Created** : avis enregistré.
* **400 Bad Request** : champs invalides.
* **404 Not Found** : utilisateur ou lieu introuvable.
* **500 Internal Server Error** : erreur interne.

<img width="627" height="703" alt="Diagramme de séquence Avis HBNB" src="https://github.com/user-attachments/assets/b2b74505-1d14-4b72-bd8a-0952cafb1962" />

---

## 4. Synthèse et portée du document

### Objectif général

Ce document sert de **référence technique complète** pour le projet HBnB. Il permet à tout membre de l’équipe de comprendre le fonctionnement et la structure du système.

### Bénéfices

* Vision claire de la structure logicielle (diagrammes de paquetage et de classes).
* Compréhension des interactions techniques (diagrammes de séquence).
* Simplification de la communication entre les membres de l’équipe.
* Réduction des erreurs pendant la phase de développement.

### Conclusion

Grâce à cette documentation, la conception de HBnB devient **plus claire, cohérente et maîtrisée**. Chaque diagramme joue un rôle précis dans la compréhension du système, de la vue d’ensemble jusqu’au détail des échanges entre les composants.

### Auteurs :

- Grégory Sala
- Lucas Blancportier
