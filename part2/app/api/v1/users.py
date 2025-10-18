from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

# Définir le modèle utilisateur pour la validation des entrées et la documentation
user_model = api.model('User', {
    'prenom': fields.String(required=True, description='First name of the user'),
    'nom': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'mot_de_passe': fields.String(required=True, description="Mot de passe de l'utilisateur"),
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        # Simuler la vérification de l'unicité des adresses e-mail (à remplacer par une validation réelle avec persistance).
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        new_user = facade.create_user(user_data)
        return {'id': new_user.id,
                'first_name': new_user.first_name,
                'last_name': new_user.last_name,
                'email': new_user.email
                }, 201

    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """Get all users"""
        users = facade.user_repo.get_all()  # récupère tous les utilisateurs dans le dépôt
        result = []

        for user in users:
            result.append({
                'id': user.id,
                'prenom': user.prenom,
                'nom': user.nom,
                'email': user.email
            })

        return result, 201

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200
    
    
    @api.expect(api.model('UserUpdate', {
        'prenom': fields.String(description='First name of the user'),
        'nom': fields.String(description='Last name of the user'),
        'email': fields.String(description='Email of the user')
    }))
    @api.response(200, 'User successfully updated')
    @api.response(404, 'User not found')
    def put(self, user_id):
        """Update an existing user"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        data = api.payload
        updated_user = facade.update_user(user_id, data)
        if not updated_user:
            return {'error': 'User not found'}, 404

        return {
            'id': updated_user.id,
            'prenom': updated_user.prenom,
            'nom': updated_user.nom,
            'email': updated_user.email
        }, 200
