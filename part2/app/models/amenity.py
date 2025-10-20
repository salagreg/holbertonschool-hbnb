from app.models.modele_base import ModeleBase
from datetime import datetime
import uuid

class Equipement(ModeleBase):
    """Classe représentant un équipement/amenity."""

    def __init__(self, nom, description="", **kwargs):
        """Initialise un nouvel équipement."""
        super().__init__(**kwargs)
        if not nom or not isinstance(nom, str):
            raise ValueError("Le nom de l’équipement doit être une chaîne non vide.")
        self.id = str(uuid.uuid4())
        self.nom = nom
        self.description = description
        self.date_creation = datetime.now().isoformat()
        self.date_mise_a_jour = datetime.now().isoformat()

    @property
    def nom(self):
        """Retourne le nom de l’équipement."""
        return self.__nom

    @nom.setter
    def nom(self, value):
        """Définit le nom de l’équipement."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Le nom de l’équipement doit être une chaîne non vide.")
        if len(value.strip()) > 50:
            raise ValueError("Le nom de l’équipement ne peut dépasser 50 caractères.")
        self.__nom = value.strip()

    @property
    def description(self):
        """Retourne la description de l’équipement."""
        return self.__description

    @description.setter
    def description(self, value):
        """Définit la description de l’équipement."""
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
        """Retourne une représentation de l’équipement sous forme de dictionnaire."""
        return {
            "id": self.id,
            "nom": self.nom,
            "description": self.description,
            "date_creation": self.date_creation,
            "date_mise_a_jour": self.date_mise_a_jour
        }

    def AjoutEquipement(self):
        """Affiche un message indiquant l’ajout de l’équipement."""
        print(f"Ajout de l’équipement : {self.nom}")

    def ModificationEquipement(self, **kwargs):
        """Met à jour l’équipement et affiche un message de modification."""
        self.update(kwargs)

    def SuppressionEquipement(self):
        """Affiche un message indiquant la suppression de l’équipement."""
        print(f"Suppression de l’équipement : {self.nom}")
