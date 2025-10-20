from app.persistence.repository import InMemoryRepository
from app.models.user import Utilisateur
from app.models.place import Lieu
from app.models.review import Avis
from app.models.amenity import Equipement

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.lieu_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        email = user_data.get('email')
        if not email:
             return {"message": "Email requis"}
        if self.get_user_by_email(email):
            return {"message": "Email déjà utilisé"}, 400
        user = Utilisateur(
        prenom=user_data.get('prenom'),
        nom=user_data.get('nom'),
        email=email,
        mot_de_passe=user_data.get('mot_de_passe'),
        is_admin=user_data.get('is_admin', False)
    )
        self.user_repo.add(user)
        return user.to_dict(include_password=False)

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    def get_all_users(self):
        users = self.user_repo.get_all()
        user_dicts = []
        for user in users:
            user_dicts.append(user.to_dict(include_password=False))
        return user_dicts
    
    def update_user(self, user_id, data):
        """
        Met à jour un utilisateur existant.
        Retourne le dict mis à jour sans mot de passe.
        """
        user = self.user_repo.get(user_id)
        if not user:
            return None
        user.update(data)
        return user.to_dict(include_password=False)
    
    def create_amenity(self, data):
        """Créer un nouvel équipement"""
        if not data.get("nom"):
            return {"message": "Nom obligatoire"}, 400
        equip = Equipement(nom=data["nom"], description=data.get("description", ""))
        self.amenity_repo.add(equip)
        return equip.to_dict()

    def get_amenity(self, amenity_id):
        """Récupérer un équipement par ID"""
        equip = self.amenity_repo.get(amenity_id)
        return equip.to_dict() if equip else None

    def get_all_amenities(self):
        """Récupérer tous les équipements"""
        return [e.to_dict() for e in self.amenity_repo.get_all()]

    def update_amenity(self, amenity_id, data):
        """Mettre à jour un équipement existant"""
        equip = self.amenity_repo.get(amenity_id)
        if not equip:
            return None  # On renvoie None, pas de tuple ici
        equip.update(data)
        return equip.to_dict()
    
    def create_lieu(self, data):
        required_fields = ["nom", "description", "prix", "latitude", "longitude", "nbr_max_voyageurs", "nbr_chambres"]
        for f in required_fields:
            if f not in data or data[f] is None:
                return {"message": f"Le champ {f} est requis"}

        # Vérifications type et valeurs
        try:
            nom = data["nom"].strip()
            description = data["description"].strip()
            prix = float(data["prix"])
            latitude = float(data["latitude"])
            longitude = float(data["longitude"])
            nbr_max_voyageurs = int(data["nbr_max_voyageurs"])
            nbr_chambres = int(data["nbr_chambres"])
        except Exception as e:
            return {"message": f"Valeurs invalides: {e}"}

        # Vérif nom unique
        if self.lieu_repo.get_by_attribute("nom", nom):
            return {"message": "Lieu déjà créé"}

        # Owner
        owner_id = data.get("owner_id")
        owner = self.user_repo.get(owner_id) if owner_id else None
        if owner_id and not owner:
            return {"message": "Propriétaire non trouvé"}

        # Amenities
        amenities_ids = data.get("amenities", [])
        lieu = Lieu(
            nom=nom,
            description=description,
            prix=prix,
            latitude=latitude,
            longitude=longitude,
            nbr_max_voyageurs=nbr_max_voyageurs,
            nbr_chambres=nbr_chambres,
            owner=owner
        )

        for aid in amenities_ids:
            amenity = self.amenity_repo.get(aid)
            if amenity:
                lieu.amenities.append(amenity)

        self.lieu_repo.add(lieu)
        return lieu.to_dict(include_owner=True, include_amenities=True)

    def get_lieu(self, lieu_id):
        lieu = self.lieu_repo.get(lieu_id)
        return lieu.to_dict(include_owner=True, include_amenities=True) if lieu else None

    def get_all_lieux(self):
        return [l.to_dict(include_owner=True, include_amenities=True) for l in self.lieu_repo.get_all()]

    def update_lieu(self, lieu_id, data):
        lieu = self.lieu_repo.get(lieu_id)
        if not lieu:
            return None
        lieu.update(data)
        return lieu.to_dict(include_owner=True, include_amenities=True)
    
    def create_review(self, review_data):
        user = self.user_repo.get(review_data.get("user_id"))
        place = self.lieu_repo.get(review_data.get("place_id"))
        if not user or not place:
            return {"message": "Utilisateur ou lieu inexistant"}, 400
        rating = review_data.get("note")
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            return {"message": "Note invalide"}, 400
        review = Avis(
        commentaire=review_data["commentaire"],
        note=rating,
        place=place,
        user=user,
        )
        self.review_repo.add(review)
        place.reviews.append(review) 
        return review.to_dict()

    def get_review(self, review_id):
        review = self.review_repo.get(review_id)
        return review.to_dict() if review else None

    def get_all_reviews(self):
        return [r.to_dict() for r in self.review_repo.get_all()]

    def get_reviews_by_place(self, place_id):
        place = self.lieu_repo.get(place_id)
        if not place:
            return None
        reviews = [r.to_dict() for r in self.review_repo.get_all() if r.place.id == place_id]
        return reviews

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)
        if not review:
            return None
        if "text" in review_data:
            review.commentaire = review_data["text"]
        if "rating" in review_data:
            rating = review_data["rating"]
            if not isinstance(rating, int) or not (1 <= rating <= 5):
                return None
            review.note = rating
        review.sauvegarder()
        return review.to_dict()

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            return None
        self.review_repo.delete(review_id)
        return True