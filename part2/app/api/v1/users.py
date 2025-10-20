from flask_restx import Namespace, Resource, fields
from app.models.user import Utilisateur
from datetime import datetime
from app.services.facade import HBnBFacade
facade = HBnBFacade()

api = Namespace('users', description='Opérations liées aux utilisateurs')

user_model = api.model('User', {
    'id': fields.String(description='ID de l’utilisateur'),
    'prenom': fields.String(required=True, description='Prénom de l’utilisateur'),
    'nom': fields.String(required=True, description='Nom de l’utilisateur'),
    'email': fields.String(required=True, description='Email de l’utilisateur'),
    'mot_de_passe': fields.String(required=True, description='Mot de passe de l’utilisateur'),
    'is_admin': fields.Boolean(description='Est administrateur'),
    'date_creation': fields.String(description='Date de création', readonly=True),
    'date_mise_a_jour': fields.String(description='Date de mise à jour', readonly=True),
})

@api.route('/')
class UserList(Resource):
    """Gestion des opérations sur la collection d'utilisateurs"""


    @api.marshal_list_with(user_model)
    def get(self):
        "Récupère la liste de tous les utilisateurs"
        return facade.get_all_users()

    @api.expect(user_model)
    @api.marshal_with(user_model, code=201)
    def post(self):
        """Crée un nouvel utilisateur"""
        data = api.payload
        user = facade.create_user(data)
        if not user:
            api.abort(400, "Email déjà utilisé")
        return user, 201

@api.route('/<string:user_id>')
class UserUpdate(Resource):
    """Gestion des opérations sur un utilisateur individuel"""

    
    @api.marshal_with(user_model)
    def get(self, user_id):
        """Récupère un utilisateur par son ID"""
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, f"Utilisateur {user_id} non trouvé")
        return user

    @api.expect(user_model)
    @api.marshal_with(user_model)
    def put(self, user_id):
        """Met à jour un utilisateur existant"""
        data = api.payload
        user = facade.update_user(user_id, data)
        if not user:
            api.abort(404, f"Utilisateur {user_id} non trouvé")
        return user
