from flask import Flask
from flask_restful import  Api
from config import Config

api = Api()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    
    import resource.api
    api.init_app(app)

    return app