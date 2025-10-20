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
    @api.marshal_list_with(user_model)
    def get(self):
        "Récupère la liste de tous les utilisateurs"
        # ici tu récupères tous les utilisateurs et tu renvoies la liste de dicts
        return facade.get_all_users()
    
    @api.expect(user_model)
    @api.marshal_with(user_model, code=201)
    def post(self):
        """Crée un nouvel utilisateur"""
        result = facade.create_user(api.payload)
        # Si create_user retourne un tuple (message, status)
        if isinstance(result, tuple):
            api.abort(result[1], result[0]["message"])
    
        # Si create_user retourne juste un dict avec message d'erreur
        elif isinstance(result, dict) and "message" in result:
            api.abort(400, result["message"])
    
        return result, 201

@api.route('/<string:user_id>')
class UserUpdate(Resource):

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
