from .modele_base import ModeleBase
import re
from datetime import datetime

class Utilisateur(ModeleBase):
    """Classe représentant un utilisateur de HBnB."""

    def __init__(self, prenom, nom, email, mot_de_passe, is_admin=False, **kwargs):
        super().__init__(**kwargs)
        self.prenom = prenom
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.is_admin = is_admin

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Le prénom doit être une chaîne non vide.")
        if len(value.strip()) > 50:
            raise ValueError("Le prénom ne peut dépasser 50 caractères.")
        self.__prenom = value.strip()

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Le nom doit être une chaîne non vide.")
        if len(value.strip()) > 50:
            raise ValueError("Le nom ne peut dépasser 50 caractères.")
        self.__nom = value.strip()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("L'email doit être une chaîne non vide.")
        # Regex plus stricte
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, value.strip()):
            raise ValueError("L'email n'est pas valide.")
        self.__email = value.strip()

    @property
    def mot_de_passe(self):
        return self.__mot_de_passe

    @mot_de_passe.setter
    def mot_de_passe(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Le mot de passe doit être une chaîne non vide.")
        self.__mot_de_passe = value.strip()

    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, value):
        if not isinstance(value, bool):
            raise TypeError("is_admin doit être un booléen.")
        self.__is_admin = value

    def to_dict(self, include_password=False):
        data = {
            "id": self.id,
            "prenom": self.prenom,
            "nom": self.nom,
            "email": self.email,
            "is_admin": self.is_admin,
            "date_creation": self.date_creation.isoformat() if isinstance(self.date_creation, datetime) else self.date_creation,
            "date_mise_a_jour": self.date_mise_a_jour.isoformat() if isinstance(self.date_mise_a_jour, datetime) else self.date_mise_a_jour
        }
        if include_password:
            data["mot_de_passe"] = self.mot_de_passe
        return data

    def CreationProfil(self):
        print(f"Création du profil : {self.prenom} {self.nom} ({self.email})")

    def ModificationProfil(self, **kwargs):
        self.update(kwargs)

    def SuppressionProfil(self):
        print(f"Suppression du profil : {self.email}")
