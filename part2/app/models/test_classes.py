#!/usr/bin/env python3
# test_classes.py
from user import Utilisateur
from place import Lieu
from review import Avis
from amenity import Equipement

def print_separator(title):
    print("\n" + "="*5 + f" {title} " + "="*5 + "\n")

def test_classes():
    print_separator("TEST UTILISATEURS")
    # Création des utilisateurs
    alice = Utilisateur(prenom="Alice", nom="Dupont", email="alice@example.com", mot_de_passe="alice123")
    bob = Utilisateur(prenom="Bob", nom="Martin", email="bob@example.com", mot_de_passe="bob123")
    
    utilisateurs = [alice, bob]
    for u in utilisateurs:
        print(f"- {u.prenom} {u.nom} ({u.email}) ID: {u.id}")

    print_separator("TEST LIEU")
    # Création d'un lieu
    appartement = Lieu(
        titre="Appartement cosy",
        description="Un super endroit pour se reposer",
        prix=120,
        latitude=48.8566,
        longitude=2.3522,
        nbr_max_voyageurs=4,
        nbr_chambres=2,
        owner=alice
    )
    print(f"{appartement.titre} ({appartement.nbr_chambres} chambres, {appartement.prix}€/nuit) - Owner: {appartement.owner.prenom}")

    print_separator("TEST AMENITIES")
    # Ajout d'amenities
    wifi = Equipement("Wi-Fi")
    parking = Equipement("Parking")
    appartement.amenities.append(wifi)
    appartement.amenities.append(parking)

    print(f"Amenities pour {appartement.titre} : {[a.nom for a in appartement.amenities]}")

    print_separator("TEST AVIS")
    # Création d'avis
    avis1 = Avis(commentaire="Super séjour !", note=5, place=appartement, user=bob)
    avis2 = Avis(commentaire="Propre et confortable", note=4, place=appartement, user=alice)
    appartement.reviews.extend([avis1, avis2])

    print(f"Avis pour {appartement.titre} : {[(r.user.prenom, r.commentaire, r.note) for r in appartement.reviews]}")

    print_separator("TEST METHODES UPDATE ET TO_DICT")
    print(f"Avant update: {appartement.prix}")
    appartement.update({"prix": 150, "nbr_chambres": 3})
    print(f"Après update: {appartement.prix} {appartement.nbr_chambres}")
    print("Dictionnaire du lieu après update:", appartement.to_dict())

    print_separator("TEST AJOUT/MODIFICATION/SUPPRESSION")
    wifi2 = Equipement("Wi-Fi Ultra Rapide")
    appartement.amenities.append(wifi2)
    wifi2.AjoutEquipement()
    wifi2.SuppressionEquipement()

    alice.CreationProfil()
    alice.SuppressionProfil()

    appartement.AjoutLieu()
    appartement.SuppressionLieu()

    avis1.RedactionAvis()
    avis1.SuppressionAvis()

    print_separator("TEST FILTRAGE")
    # Filtrage de lieux
    maison = Lieu(
        titre="Maison familiale",
        description="Grande maison avec jardin",
        prix=250,
        latitude=48.8566,
        longitude=2.3522,
        nbr_max_voyageurs=6,
        nbr_chambres=3,
        owner=bob
    )
    lieux = [appartement, maison]
    lieux_filtrés = Lieu.filtrer(lieux, nbr_chambres=2)
    print(f"Lieux filtrés (nbr_chambres>=2): {[l.titre for l in lieux_filtrés]}")

    print_separator("TEST VALIDATION ERREURS")
    try:
        Avis(commentaire="", note=3, place=appartement, user=alice)
    except ValueError as e:
        print(f"Erreur attendue (commentaire vide): {e}")

    try:
        Avis(commentaire="Ok", note=6, place=appartement, user=alice)
    except ValueError as e:
        print(f"Erreur attendue (note > 5): {e}")

    try:
        maison.update({"description": ""})
    except ValueError as e:
        print(f"Erreur attendue (attributs invalides): {e}")

if __name__ == "__main__":
    print_separator("STRESS TEST DES CLASSES HBnB")
    test_classes()
