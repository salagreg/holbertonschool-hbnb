from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

facade = HBnBFacade()

api = Namespace('Reviews', description='Opérations liées aux avis')

review_model = api.model('Review', {
    'id': fields.String(readonly=True),
    'commentaire': fields.String(required=True, description="Contenu de l’avis"),
    'note': fields.Integer(required=True, description="Note entre 0 et 5"),
    'user_id': fields.String(required=True, description="ID de l’utilisateur auteur"),
    'place_id': fields.String(required=True, description="ID du lieu concerné")
})

@api.route('/')
class ReviewList(Resource):
    @api.marshal_list_with(review_model)
    def get(self):
        """Récupère tous les avis"""
        return facade.get_all_reviews()

    @api.expect(review_model)
    @api.marshal_with(review_model, code=201)
    def post(self):
        """Crée un nouvel avis"""
        data = api.payload
        review = facade.create_review(data)
        if not review:
            api.abort(400, "Impossible de créer l’avis (utilisateur ou lieu invalide)")
        return review, 201


@api.route('/<string:review_id>')
class ReviewDetail(Resource):
    @api.marshal_with(review_model)
    def get(self, review_id):
        """Récupère un avis par ID"""
        review = facade.get_review(review_id)
        if not review:
            api.abort(404, "Avis non trouvé")
        return review
    def delete(self, review_id):
        """Supprime un avis"""
        result = facade.delete_review(review_id)
        if not result:
            api.abort(404, "Avis non trouvé")
        return {"message": "Avis supprimé avec succès"}, 200

    @api.expect(review_model)
    @api.marshal_with(review_model)
    def put(self, review_id):
        """Met à jour un avis"""
        data = api.payload
        review = facade.update_review(review_id, data)
        if not review:
            api.abort(404, "Avis non trouvé")
        return review
    
@api.route('/places/<string:place_id>/reviews')
class PlaceReviewList(Resource):
    @api.marshal_list_with(review_model)
    def get(self, place_id):
        """Récupère tous les avis pour un lieu spécifique"""
        reviews = facade.get_reviews_by_place(place_id)
        if reviews is None:
            api.abort(404, "Lieu non trouvé")
        return reviews
