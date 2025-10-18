from flask import request
from flask_restx import Namespace, Resource, fields
from app.services import HBnBFacade

api = Namespace('amenities', description='Opérations liées aux équipements')
facade = HBnBFacade()


# Modèle pour Swagger et validation d’entrée
amenity_model = api.model('Amenity', {
    'nom': fields.String(required=True, description='Nom de l’équipement'),
    'description': fields.String(description='Description optionnelle')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Équipement créé avec succès')
    @api.response(400, 'Entrée invalide')
    def post(self):
        """Créer un nouvel équipement"""
        data = api.payload
        result, status = facade.create_amenity(data)
        return result, status

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Liste des équipements récupérée avec succès"""
        result, status = facade.get_all_amenities()
        return result, status

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Équipement trouvé')
    @api.response(404, 'Équipement non trouvé')
    def get(self, amenity_id):
        """Obtenir un équipement par ID"""
        result, status = facade.get_amenity(amenity_id)
        return result, status


    @api.expect(amenity_model)
    @api.response(200, 'Équipement mis à jour avec succès')
    @api.response(404, 'Équipement non trouvé')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Mettre à jour un équipement existant"""
        data = api.payload
        result, status = facade.update_amenity(amenity_id, data)
        return result, status
    
@api.route('/amenities')
class AmenityList(Resource):
    def get(self):
        return AmenityFacade().get_all_amenities()

    def post(self):
        data = request.get_json()
        return AmenityFacade().create_amenity(data)

@api.route('/amenities/<amenity_id>')
class AmenityResource(Resource):
    def get(self, amenity_id):
        return AmenityFacade().get_amenity(amenity_id)

    def put(self, amenity_id):
        data = request.get_json()
        return AmenityFacade().update_amenity(amenity_id, data)
