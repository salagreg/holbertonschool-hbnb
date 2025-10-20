from modele_base import ModeleBase
from user import Utilisateur
from place import Lieu

class Avis(ModeleBase):
    """Classe représentant un avis laissé par un utilisateur sur un lieu."""

    def __init__(self, commentaire, note, place, user, **kwargs):
        """Initialise un nouvel avis avec validation des champs."""
        super().__init__(**kwargs)
        self.commentaire = commentaire
        self.note = note
        self.place = place
        self.user = user

    @property
    def commentaire(self):
        """Retourne le commentaire de l'avis."""
        return self.__commentaire

    @commentaire.setter
    def commentaire(self, value):
        """Définit et valide le commentaire (chaîne non vide)."""
        if not isinstance(value, str):
            raise TypeError("Le commentaire doit être une chaîne de caractères.")
        if not value.strip():
            raise ValueError("Le commentaire ne peut pas être vide.")
        self.__commentaire = value.strip()

    @property
    def note(self):
        """Retourne la note associée à l'avis."""
        return self.__note

    @note.setter
    def note(self, value):
        """Définit et valide la note (entier entre 1 et 5)."""
        if not isinstance(value, int):
            raise TypeError("La note doit être un entier.")
        if not (1 <= value <= 5):
            raise ValueError("La note doit être comprise entre 1 et 5.")
        self.__note = value

    @property
    def place(self):
        """Retourne le lieu concerné par l'avis."""
        return self.__place

    @place.setter
    def place(self, value):
        """Définit et valide le lieu concerné."""
        if not isinstance(value, Lieu):
            raise TypeError("place doit être une instance de Lieu.")
        self.__place = value

    @property
    def user(self):
        """Retourne l'utilisateur ayant rédigé l'avis."""
        return self.__user

    @user.setter
    def user(self, value):
        """Définit et valide l'auteur de l'avis."""
        if not isinstance(value, Utilisateur):
            raise TypeError("user doit être une instance de Utilisateur.")
        self.__user = value

    def update(self, data):
        """Met à jour les attributs de l'avis avec les données fournies."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.sauvegarder()
        return self

    def to_dict(self):
        """Convertit l'avis en dictionnaire sérialisable."""
        return {
            "id": self.id,
            "commentaire": self.commentaire,
            "note": self.note,
            "place_id": self.place.id,
            "user_id": self.user.id,
            "date_creation": self.date_creation,
            "date_mise_a_jour": self.date_mise_a_jour
        }

    def RedactionAvis(self):
        """Affiche un message lors de la création d’un nouvel avis."""
        print(f"Nouvel avis : {self.commentaire} (note : {self.note}/5)")

    def SuppressionAvis(self):
        """Affiche un message lors de la suppression d’un avis."""
        print(f"Suppression de l’avis : {self.commentaire}")
