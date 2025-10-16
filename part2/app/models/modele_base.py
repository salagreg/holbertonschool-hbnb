#!/usr/bin/python3
import uuid
from datetime import datetime

class ModeleBase:
    _instances = {}
    def __init__(self, id=None, date_creation=None, date_mise_a_jour=None):
        self.id = id or str(uuid.uuid4())
        self.date_creation = date_creation or datetime.now()
        self.date_mise_a_jour = date_mise_a_jour or datetime.now()
    
    # Ajouter l'instance au stockage centralisé
        cls = type(self)
        if cls not in ModeleBase._instances:
            ModeleBase._instances[cls] = {}
        ModeleBase._instances[cls][self.id] = self

    def sauvegarder(self):
        self.date_mise_a_jour = datetime.now()
    
    def update(self, data):
        """Met à jour les attributs de l'objet depuis un dictionnaire."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.sauvegarder()
        return self

    @staticmethod
    def is_max_length(nom_attribut, valeur, longueur_max):
        """Vérifie que la chaîne n’excède pas la longueur max."""
        if len(valeur) > longueur_max:
            raise ValueError(f"{nom_attribut} ne peut pas dépasser {longueur_max} caractères.")


    @classmethod
    def all(cls):
        """Retourne toutes les instances de cette classe."""
        return list(ModeleBase._instances.get(cls, {}).values())

    @classmethod
    def get_by_id(cls, id_):
        """Retourne l'instance de cette classe avec l'ID donné."""
        return ModeleBase._instances.get(cls, {}).get(id_)
    
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
