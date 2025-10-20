from abc import ABC, abstractmethod

class Repository(ABC):
    """Classe abstraite définissant l'interface d'un dépôt."""


    @abstractmethod
    def add(self, obj):
        """Ajoute un nouvel objet au dépôt."""
        pass

    @abstractmethod
    def get(self, obj_id):
        """Récupère un objet à partir de son identifiant unique."""
        pass

    @abstractmethod
    def get_all(self):
        """Récupère tous les objets présents dans le dépôt."""
        pass

    @abstractmethod
    def update(self, obj_id, data):
        """Met à jour un objet existant dans le dépôt."""
        pass

    @abstractmethod
    def delete(self, obj_id):
        """Supprime un objet du dépôt."""
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        """Recherche un objet par un attribut spécifique."""
        pass


class InMemoryRepository:
    """Implémentation concrète du dépôt en mémoire."""


    def __init__(self):
        """Initialise un dépôt vide stockant les objets en mémoire."""
        self._data = {}

    def add(self, obj):
        """Ajoute un objet au dépôt en l’indexant par son identifiant."""
        self._data[obj.id] = obj
        return obj

    def get(self, obj_id):
        """Récupère un objet par son identifiant."""
        return self._data.get(obj_id)

    def get_all(self):
        """Récupère la liste de tous les objets stockés."""
        return list(self._data.values())

    def get_by_attribute(self, attr, value):
        """Recherche un objet dont un attribut correspond à une valeur donnée."""
        for obj in self._data.values():
            if hasattr(obj, attr) and getattr(obj, attr) == value:
                return obj
        return None
