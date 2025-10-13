from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Méthode de remplacement pour créer un utilisateur
    def create_user(self, user_data):
        # La logique sera mise en œuvre dans les tâches ultérieures.
        pass

    # Méthode de remplacement pour récupérer un lieu par son identifiant
    def get_place(self, place_id):
        # La logique sera mise en œuvre dans les tâches ultérieures.
        pass
