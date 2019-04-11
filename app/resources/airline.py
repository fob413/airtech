from flask_restful import Resource
from flask import request, g, jsonify

from app.models.airline import Airline
from app.models.user import User
from app.utils.validator import Validator
from app.utils.tools import (
    success_response,
    error_response
)


class Airlines(Resource):
    
    @Validator.validate_admin_token()
    @Validator.validate([
        'name|required:str',
        'nameAbb|required:str'
    ])
    @Validator.validate_airline()
    def post(self):
        payload = request.get_json()
        
        new_airline = Airline(
            name = payload['name'],
            name_abb = payload['nameAbb']
        )
        new_airline.save()
        new_airline = new_airline.serialize()

        return success_response(new_airline, 201)
