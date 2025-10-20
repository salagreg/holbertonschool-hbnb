import requests

BASE_URL = "http://127.0.0.1:5000/api/v1"

# === TEST UTILISATEURS ===
print("=== TEST UTILISATEURS ===")

user_payload = {
    "prenom": "Alice",
    "nom": "Smith",
    "email": "alice@example.com",
    "mot_de_passe": "password123",
    "is_admin": False
}

r = requests.post(f"{BASE_URL}/users/", json=user_payload)
if r.status_code == 201:
    print("POST /users/ => 201")
    user_data = r.json()
    print(user_data)
    owner_id = user_data["id"]
else:
    print("❌ Échec création utilisateur")
    print(r.json())

# GET utilisateurs
r_users = requests.get(f"{BASE_URL}/users/")
print("GET /users/ =>", r_users.status_code)
print(r_users.json())

# === TEST EQUIPEMENTS ===
print("\n=== TEST EQUIPEMENTS ===")

amenity_payloads = [
    {"nom": "Wi-Fi", "description": "Internet rapide"},
    {"nom": "Piscine", "description": "Piscine chauffée"}
]

amenity_ids = []
for payload in amenity_payloads:
    r = requests.post(f"{BASE_URL}/amenities/", json=payload)
    if r.status_code == 201:
        amenity = r.json()
        amenity_ids.append(amenity["id"])
        print("POST /amenities/ => 201", amenity)
    else:
        print("❌ Échec création équipement", r.json())

# GET équipements
r_amenities = requests.get(f"{BASE_URL}/amenities/")
print("GET /amenities/ =>", r_amenities.status_code)
print(r_amenities.json())

# === TEST LIEUX ===
print("\n=== TEST LIEUX ===")

place_payload = {
    "nom": "Chalet Montagne",
    "description": "Un chalet cosy à la montagne",
    "prix": 120.0,
    "latitude": 45.9237,
    "longitude": 6.8694,
    "nbr_max_voyageurs": 5,
    "nbr_chambres": 3,
    "owner_id": owner_id
}

r_place = requests.post(f"{BASE_URL}/places/", json=place_payload)
if r_place.status_code == 201:
    place_id = r_place.json().get("id")
else:
    print("❌ Échec création lieu")
    print(r_place.json())


# GET lieux
r_places = requests.get(f"{BASE_URL}/places/")
print("GET /places/ =>", r_places.status_code)
print(r_places.json())

# === TEST AVIS ===
print("\n=== TEST AVIS ===")

# Récupération du premier lieu et utilisateur existants
places = requests.get(f"{BASE_URL}/places/").json()
users = requests.get(f"{BASE_URL}/users/").json()

if not places:
    print("❌ Aucun lieu trouvé. Impossible de créer un avis.")
elif not users:
    print("❌ Aucun utilisateur trouvé. Impossible de créer un avis.")
else:
    place_id = places[0]["id"]
    user_id = users[0]["id"]

    review_payload = {
        "texte": "Super séjour, très agréable !",
        "note": 5,
        "user_id": user_id,
        "place_id": place_id
    }

    r_review = requests.post(f"{BASE_URL}/reviews/", json=review_payload)

    if r_review.status_code == 201:
        print("✅ Avis créé :", r_review.json())
    else:
        print("❌ Échec création avis", r_review.status_code, r_review.text)

    # Afficher tous les avis pour vérifier
    r_all_reviews = requests.get(f"{BASE_URL}/reviews/").json()
    print("Liste des avis :", r_all_reviews)