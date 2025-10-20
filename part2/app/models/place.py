from .modele_base import ModeleBase
from app.models.amenity import Equipement as Amenity
from app.models.user import Utilisateur
from uuid import uuid4

class Lieu(ModeleBase):
    """Classe représentant un lieu proposé sur HBnB."""

    def __init__(self, nom, description, prix, latitude, longitude, nbr_max_voyageurs, nbr_chambres, owner=None, **kwargs):
        super().__init__(**kwargs)
        self.id = str(uuid4())
        self.nom = nom
        self.description = description
        self.prix = prix
        self.latitude = latitude
        self.longitude = longitude
        self.nbr_max_voyageurs = nbr_max_voyageurs
        self.nbr_chambres = nbr_chambres
        self.owner = owner # instance de Utilisateur
        self.reviews = []  # liste de Review
        self.amenities = []  # liste de Amenity
    
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, value):
        if not isinstance(value, str):
            raise TypeError("Le titre doit être une chaîne de caractères.")
        if not value.strip():
            raise ValueError("Le titre ne peut pas être vide.")
        super().is_max_length("Nom", value, 100)
        self.__nom = value.strip()
    
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("La description doit être une chaîne de caractères.")
        if not value.strip():
            raise ValueError("La description ne peut pas être vide.")
        self.__description = value.strip()

    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Le prix doit être un nombre.")
        if value < 0:
            raise ValueError("Le prix ne peut pas être négatif.")
        self.__prix = float(value)
    
    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("La latitude doit être un nombre.")
        if not (-90 <= value <= 90):
            raise ValueError("La latitude doit être comprise entre -90 et 90.")
        self.__latitude = float(value)
    
    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("La longitude doit être un nombre.")
        if not (-180 <= value <= 180):
            raise ValueError("La longitude doit être comprise entre -180 et 180.")
        self.__longitude = float(value)

    @property
    def nbr_max_voyageurs(self):
        return self.__nbr_max_voyageurs

    @nbr_max_voyageurs.setter
    def nbr_max_voyageurs(self, value):
        if not isinstance(value, int):
            raise TypeError("Le nombre maximum de voyageurs doit être un entier.")
        if value <= 0:
            raise ValueError("Le nombre maximum de voyageurs doit être positif.")
        self.__nbr_max_voyageurs = value
    
    @property
    def nbr_chambres(self):
        return self.__nbr_chambres

    @nbr_chambres.setter
    def nbr_chambres(self, value):
        if not isinstance(value, int):
            raise TypeError("Le nombre de chambres doit être un entier.")
        if value < 0:
            raise ValueError("Le nombre de chambres ne peut pas être négatif.")
        self.__nbr_chambres = value
    
    @property
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self, value):
        if value is not None and not isinstance(value, Utilisateur):
            raise TypeError("owner doit être une instance de User ou None")
        self.__owner = value

    
    @classmethod
    def filtrer(cls, lieux, latitude=None, longitude=None, nbr_chambres=None, prix=None):
        resultats = []
        for lieu in lieux:
            if latitude is not None and lieu.latitude != latitude:
                continue
            if longitude is not None and lieu.longitude != longitude:
                continue
            if nbr_chambres is not None and lieu.nbr_chambres < nbr_chambres:
                continue
            if prix is not None and lieu.prix > prix:
                continue
            resultats.append(lieu)
        return resultats
    
    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.sauvegarder()
        return self
    
    def to_dict(self, include_owner=False, include_amenities=False):
        data ={
            "id": self.id,
            "nom": self.nom,
            "description": self.description,
            "prix": self.prix,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "nbr_max_voyageurs": self.nbr_max_voyageurs,
            "nbr_chambres": self.nbr_chambres,
            "owner_id": self.owner.id if self.owner else None,
            "reviews": [r.id for r in self.reviews],
            "amenities": [a.id for a in self.amenities],
        }
        if include_owner and self.owner:
            data["owner"] = {
                "id": self.owner.id,
                "first_name": self.owner.prenom,
                "last_name": self.owner.nom,
                "email": self.owner.email
            }
        if include_amenities and self.amenities:
            data["amenities"] = [
                {"id": a.id, "nom": getattr(a, "nom", "Inconnu")} 
                for a in self.amenities
            ]
        return data
    
    def AjoutLieu(self):
        print(f"Ajout du lieu : {self.titre}")

    def ModificationLieu(self, **kwargs):
        self.update(kwargs)

    def SuppressionLieu(self):
        print(f"Suppression du lieu : {self.titre}")
