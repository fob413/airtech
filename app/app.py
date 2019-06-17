from flask import Flask
from flask_restful import Resource, Api


from app.config import app_config
from app.utils.db import db
from app.resources.authentication import Signup, Signin
from app.resources.profile import Profile
from app.resources.airline import Airlines, Single_Airline
from app.resources.flight import FlightResource, Single_FlightResource, Flight_By_Location
from app.resources.flight_seat import FlightSeat
from app.resources.ticket import TicketResource
from app.resources.booked import BookedResource


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

    # user upload profile picture
    api.add_resource(Profile, '/api/v1/profile-picture')

    # admin add airline
    api.add_resource(Airlines, '/api/v1/airline')

    # admin access to single airline
    api.add_resource(Single_Airline, '/api/v1/airline/<string:airline_id>')

    # admin access to flight
    api.add_resource(FlightResource, '/api/v1/flight')

    # admin access to single flight
    api.add_resource(Single_FlightResource, '/api/v1/flight/<string:flight_id>')

    # user get flights by location
    api.add_resource(Flight_By_Location, '/api/v1/flight/location/<string:from_location>/<string:to_location>')

    # user get available flight seats
    api.add_resource(FlightSeat, '/api/v1/flight/<string:flight_code>/seats')

    # user booking resource
    api.add_resource(TicketResource, '/api/v1/ticket')

    # admin booked flight users
    api.add_resource(BookedResource, '/api/v1/flight/<string:flight_id>/booked')

    return app
