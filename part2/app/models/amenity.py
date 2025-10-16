from app.models.modele_base import ModeleBase

class Equipement(ModeleBase):
    """Classe représentant un équipement/amenity."""

    def __init__(self, nom, description="", **kwargs):
        super().__init__(**kwargs)
        self.nom = nom
        self.description = description

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Le nom de l’équipement doit être une chaîne non vide.")
        if len(value.strip()) > 50:
            raise ValueError("Le nom de l’équipement ne peut dépasser 50 caractères.")
        self.__nom = value.strip()

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
        return {
            "id": self.id,
            "nom": self.nom,
            "description": self.description,
            "date_creation": self.date_creation,
            "date_mise_a_jour": self.date_mise_a_jour
        }

    def AjoutEquipement(self):
        print(f"Ajout de l’équipement : {self.nom}")

    def ModificationEquipement(self, **kwargs):
        self.update(kwargs)

    def SuppressionEquipement(self):
        print(f"Suppression de l’équipement : {self.nom}")
