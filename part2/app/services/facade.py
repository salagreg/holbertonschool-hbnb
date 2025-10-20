from app.persistence.repository import InMemoryRepository
from app.models.user import Utilisateur
from app.models.amenity import Equipement
from app.models.place import Lieu

class HBnBFacade:
    """Classe de façade principale de l'application HBnB."""


    def __init__(self):
        """Initialise les dépôts en mémoire pour chaque type d'entité."""
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.lieu_repo = InMemoryRepository()

    def create_user(self, user_data):
        """Crée un nouvel utilisateur à partir des données fournies."""
        if self.get_user_by_email(user_data['email']):
            return None  
        user = Utilisateur(**user_data)
        self.user_repo.add(user)
        return user.to_dict(include_password=False)

    def get_user(self, user_id):
        """Récupère un utilisateur à partir de son identifiant unique."""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """Recherche un utilisateur par son adresse e-mail."""
        return self.user_repo.get_by_attribute('email', email)
    
    def get_all_users(self):
        """Récupère la liste complète des utilisateurs enregistrés."""
        users = self.user_repo.get_all()
        user_dicts = []
        for user in users:
            user_dicts.append(user.to_dict(include_password=False))
        return user_dicts
    
    def update_user(self, user_id, data):
        """Met à jour les informations d’un utilisateur existant."""
        user = self.user_repo.get(user_id)
        if not user:
            return None
        user.update(data)
        return user.to_dict(include_password=False)

    def create_amenity(self, data):
        """Créer un nouvel équipement"""
        if not data.get("nom"):
            raise ValueError("Le nom de l’équipement est obligatoire.")
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
            return None
        equip.update(data)
        return equip.to_dict()

    def create_lieu(self, data):
        """Crée un nouveau lieu à partir des données fournies."""
        for lieu in self.lieu_repo.get_all():
            if (lieu.latitude == data['latitude'] and 
                lieu.longitude == data['longitude'] and 
                lieu.owner and lieu.owner.id == data.get('owner_id')):
                return None 

        owner = None
        owner_id = data.get("owner_id")
        if owner_id:
            owner = self.user_repo.get(owner_id)
            if not owner:
                return None
        data["owner"] = owner
        try:
            lieu = Lieu(**data)
        except (TypeError, ValueError) as e:
            print(f"Erreur de validation lors de la création du lieu : {e}")
            return None
        self.lieu_repo.add(lieu)
        return lieu.to_dict()

    def get_lieu(self, lieu_id):
        """Récupère un lieu à partir de son identifiant."""
        lieu = self.lieu_repo.get(lieu_id)
        return lieu.to_dict(include_owner=True, include_amenities=True) if lieu else None

    def get_all_lieux(self):
        """Récupère la liste complète des lieux enregistrés."""
        return [l.to_dict(include_owner=True, include_amenities=True) for l in self.lieu_repo.get_all()]

    def update_lieu(self, lieu_id, data):
        """Met à jour les informations d’un lieu existant."""
        lieu = self.lieu_repo.get(lieu_id)
        if not lieu:
            return None
        lieu.update(data)
        return lieu.to_dict(include_owner=True, include_amenities=True)
