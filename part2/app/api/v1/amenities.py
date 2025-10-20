from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('amenities', description='Gestion des équipements')
facade = HBnBFacade()

# Modèle Swagger (en français)
amenity_model = api.model('Amenity', {
    'nom': fields.String(required=True, description="Nom de l’équipement"),
    'description': fields.String(required=False, description="Description de l'équipement")
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Équipement créé avec succès')
    @api.response(400, 'Entrée invalide')
    def post(self):
        """Créer un nouvel équipement"""
        data = api.payload
        if not data or not data.get("nom"):
            return {"message": "Le champ 'nom' est requis."}, 400

        new_amenity = facade.create_amenity(data)
        return new_amenity, 201
    
    @api.response(200, 'Liste des équipements récupérée avec succès')
    def get(self):
        """Récupérer la liste de tous les équipements"""
        return facade.get_all_amenities(), 200


@api.route('/<string:amenity_id>')
@api.param('amenity_id', 'ID de l’équipement')
class AmenityResource(Resource):
    @api.response(200, 'Détails de l’équipement récupérés avec succès')
    @api.response(404, 'Équipement non trouvé')
    def get(self, amenity_id):
        """Récupérer un équipement par ID"""
        equip = facade.get_amenity(amenity_id)
        if not equip:
            return {"message": "Équipement non trouvé"}, 404
        return equip, 200

    @api.expect(amenity_model)
    @api.response(200, 'Équipement mis à jour avec succès')
    @api.response(404, 'Équipement non trouvé')
    @api.response(400, 'Données invalides')
    def put(self, amenity_id):
        """Mettre à jour un équipement"""
        data = api.payload
        if not data or not data.get("nom"):
            return {"message": "Le champ 'nom' est requis."}, 400

        updated = facade.update_amenity(amenity_id, data)
        if not updated:
            return {"message": "Équipement non trouvé"}, 404

        return updated, 200
