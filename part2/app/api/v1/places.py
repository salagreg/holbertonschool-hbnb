from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
facade = HBnBFacade()

api = Namespace('Lieux', description='Opérations liées aux Lieux')

lieu_model = api.model('Lieu', {
    'id': fields.String(description='ID du lieu'),
    'titre': fields.String(required=True, description='Nom du Lieu'),
    'description': fields.String(required=True, description='Description du lieu'),
    'prix': fields.Float(required=True, description='Prix'),
    'latitude': fields.Float(required=True, description='Adresse Y'),
    'longitude': fields.Float(required=True, description='Adresse X'),
    'nbr_max_voyageurs': fields.Integer(description='Nombre de voyageurs maximum'),
    'nbr_chambres': fields.Integer(description='Nombres de chambres'),
    'amenities': fields.List(fields.String, description='Equipements du lieu', readonly=True),
    'reviews': fields.List(fields.String, description='Avis', readonly=True),
    })

@api.route('/')
class Lieulist(Resource):
    @api.marshal_list_with(lieu_model)
    def get(self):
        """Récupère la liste de tous les lieux"""
        return facade.get_all_lieux()

    @api.expect(lieu_model)
    @api.marshal_with(lieu_model, code=201)
    def post(self):
        """Crée un nouveau lieu"""
        data = api.payload
        lieu = facade.create_lieu(data)
        if not lieu:
            api.abort(400, "lieu déjà crée")
        return lieu, 201

@api.route('/<string:lieu_id>')
class LieuDetail(Resource):

    @api.marshal_with(lieu_model)
    def get(self, lieu_id):
        """Récupère un lieu par son ID"""
        lieu = facade.get_lieu(lieu_id)
        if not lieu:
            api.abort(404, f"Lieu {lieu_id} non trouvé")
        return lieu

    @api.expect(lieu_model)
    @api.marshal_with(lieu_model)
    def put(self, lieu_id):
        """Met à jour un lieu existant"""
        data = api.payload
        lieu = facade.update_lieu(lieu_id, data)
        if not lieu:
            api.abort(404, f"Lieu {lieu_id} non trouvé")
        return lieu
