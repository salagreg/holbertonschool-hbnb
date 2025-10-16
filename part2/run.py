from flask import Flask
from flask_restx import Api
from app.api.v1.places import api as lieu_ns

app = Flask(__name__)
api = Api(app, title="HBnB API", version="1.0", description="API de gestion des lieux et utilisateurs")

# Enregistre le namespace
api.add_namespace(lieu_ns, path="/lieux")

if __name__ == "__main__":
    app.run(debug=True)
