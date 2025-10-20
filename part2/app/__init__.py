from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as lieux_ns

def create_app():
    """Fonction de création et de configuration principale de l'application Flask."""
    app = Flask(__name__)
    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='HBnB Application API',
        doc='/api/v1/'
    )

    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(lieux_ns, path='/api/v1/lieux')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')

    return app
