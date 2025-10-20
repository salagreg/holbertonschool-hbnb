from app.models.modele_base import ModeleBase
from datetime import datetime, timezone


class Equipement(ModeleBase):
    """Classe représentant un équipement/amenity."""

    def __init__(self, nom, description="", date_creation=None, date_mise_a_jour=None, **kwargs):
        super().__init__(**kwargs)
        self.nom = nom
        self.description = description
        self.date_creation = date_creation or datetime.now(timezone.utc)
        self.date_mise_a_jour = date_mise_a_jour or datetime.now(timezone.utc)

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Le nom de l’équipement doit être une chaîne non vide.")
        cleaned = value.strip()
        if len(cleaned) > 50:
            cleaned = cleaned[:50]
        self.__nom = cleaned

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("La description doit être une chaîne de caractères.")
        self.__description = value.strip()

    def update(self, data):
        """Met à jour les attributs depuis un dictionnaire."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.sauvegarder()
        return self

    def to_dict(self):
        """Convertit l’objet en dictionnaire JSON-compatible."""
        return {
            "id": self.id,
            "nom": self.nom,
            "description": self.description,
            "date_creation": self.date_creation.isoformat() if self.date_creation else None,
            "date_mise_a_jour": self.date_mise_a_jour.isoformat() if self.date_mise_a_jour else None
        }

    def AjoutEquipement(self):
        print(f"Ajout de l’équipement : {self.nom}")

    def ModificationEquipement(self, **kwargs):
        self.update(kwargs)

    def SuppressionEquipement(self):
        print(f"Suppression de l’équipement : {self.nom}")
