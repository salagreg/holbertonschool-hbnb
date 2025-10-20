import pytest
from app.services.facade import HBnBFacade
from app.models.place import Lieu

@pytest.fixture
def facade():
    return HBnBFacade()

def test_users_api(facade):
    # Création utilisateur valide
    user = facade.create_user({
        "prenom": "John",
        "nom": "Doe",
        "email": "john@example.com",
        "mot_de_passe": "pass"
    })
    assert user["prenom"] == "John"

    # Création utilisateur avec email déjà utilisé
    dup_user = facade.create_user({
        "prenom": "Jane",
        "nom": "Doe",
        "email": "john@example.com",
        "mot_de_passe": "pass2"
    })
    assert dup_user is None

    # Récupération liste utilisateurs
    users = facade.get_all_users()
    assert len(users) == 1

    # Récupération utilisateur par ID
    fetched = facade.get_user(user["id"])
    assert fetched.id == user["id"]

    # Mise à jour utilisateur
    updated = facade.update_user(user["id"], {"prenom": "Johnny"})
    assert updated["prenom"] == "Johnny"

def test_places_api(facade):
    # Création owner
    owner = facade.create_user({
        "prenom": "Owner",
        "nom": "Test",
        "email": "owner@example.com",
        "mot_de_passe": "pass"
    })

    # Création lieu valide
    lieu_data = {
        "titre": "Maison Test",
        "description": "Une jolie maison",
        "prix": 120,
        "latitude": 48.85,
        "longitude": 2.35,
        "nbr_max_voyageurs": 4,
        "nbr_chambres": 2,
        "owner_id": owner["id"]
    }
    lieu = facade.create_lieu(lieu_data)
    assert lieu["titre"] == "Maison Test"

    # Création lieu owner inexistant
    invalid_lieu = facade.create_lieu({**lieu_data, "owner_id": "x"})
    assert invalid_lieu is None

    # Récupération tous lieux
    all_lieux = facade.get_all_lieux()
    assert len(all_lieux) == 1

    # Récupération par ID
    fetched = facade.get_lieu(lieu["id"])
    assert fetched["id"] == lieu["id"]

    # Update valide
    updated = facade.update_lieu(lieu["id"], {"prix": 150})
    assert updated["prix"] == 150

    # Update invalide
    assert facade.update_lieu("x", {"prix": 0}) is None

    # Filtrage via classe Lieu
    filtered = Lieu.filtrer([facade.lieu_repo.get(lieu["id"])], prix=200)
    assert len(filtered) == 1

def test_reviews_api(facade):
    # Créer user et lieu
    user = facade.create_user({
        "prenom": "Alice",
        "nom": "Test",
        "email": "alice@example.com",
        "mot_de_passe": "pass"
    })
    lieu = facade.create_lieu({
        "titre": "Villa Alice",
        "description": "Villa test",
        "prix": 200,
        "latitude": 48.85,
        "longitude": 2.35,
        "nbr_max_voyageurs": 4,
        "nbr_chambres": 2,
        "owner_id": user["id"]
    })

    # Création review valide
    review_data = {
        "texte": "Super séjour !",
        "rating": 5,
        "user_id": user["id"],
        "place_id": lieu["id"]
    }
    review = facade.create_review(review_data)
    assert review["commentaire"] == "Super séjour !"
    assert review["note"] == 5

    # Mise à jour review
    updated = facade.update_review(review["id"], {"rating": 4, "texte": "Très bien"})
    assert updated["note"] == 4
    assert updated["commentaire"] == "Très bien"

    # Récupération review par ID
    fetched = facade.get_review(review["id"])
    assert fetched["id"] == review["id"]

    # Récupération reviews par lieu
    reviews_for_place = facade.get_reviews_by_place(lieu["id"])
    assert len(reviews_for_place) == 1

    # Suppression review
    deleted = facade.delete_review(review["id"])
    assert deleted is True
    assert facade.get_review(review["id"]) is None
