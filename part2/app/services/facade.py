from app.persistence.repository import InMemoryRepository
from app.models.user import Utilisateur

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()

    def create_user(self, user_data):
        if self.get_user_by_email(user_data['email']):
            return None  # email déjà utilisé
        user = Utilisateur(**user_data)
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
