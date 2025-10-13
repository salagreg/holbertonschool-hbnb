from flask import Flask
from flask_restx import Api

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/')

    # Espace réservé pour les espaces de noms API (les points de terminaison seront ajoutés ultérieurement)
    # Des espaces de noms supplémentaires pour les lieux, les avis et les équipements seront ajoutés ultérieurement

    return app
