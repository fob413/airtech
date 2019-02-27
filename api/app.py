from flask import Flask
from flask_restful import Resource, Api


from api.config import app_config
from api.utils.db import db
from api.resources.authentication import Signup, Signin


def create_app(env_name):
    """
    Create app
    """

    app = Flask(__name__)
    app.config.from_object(app_config[env_name])

    db.init_app(app)

    api = Api(app)

    class HelloWorld(Resource):
        def get(self):
            return {'message': 'Welcome to Airtech'}




    api.add_resource(HelloWorld, '/')

    # user sign up endpoint
    api.add_resource(Signup, '/api/v1/auth/signup')

    # user sign in endpoint
    api.add_resource(Signin, '/api/v1/auth/signin')

    return app
