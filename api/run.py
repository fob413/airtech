from flask import Flask
from flask_restful import Resource, Api


from api.config import app_config


def create_app(env_name):
    """
    Create app
    """

    app = Flask(__name__)
    app.config.from_object(app_config[env_name])

    api = Api(app)

    class HelloWorld(Resource):
        def get(self):
            return {'message': 'Hello World'}


    api.add_resource(HelloWorld, '/')

    return app
