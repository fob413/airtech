from flask_restful import Resource
from flask import request

from api.models.user import User
from api.utils.validator import Validator
from api.utils.tools import (
    generate_hash,
    error_response,
    generate_token,
    success_response
)


class Signup(Resource):
    """
    Create new user
    """
    
    @Validator.validate([
        'firstname|required:str',
        'lastname|required:str',
        'email|required:str',
        'tel|required:int',
        'password|required:str',
    ])
    @Validator.validate_user()
    def post(self):
        payload = request.get_json()

        new_user = User(
            firstname = payload['firstname'].strip(),
            lastname = payload['lastname'].strip(),
            email = payload['email'].strip(),
            tel = payload['tel'].strip(),
            password = generate_hash(payload['password']),
            is_admin = False
        )
        new_user.save()

        if new_user.id:
            token = generate_token(new_user.id)

            return success_response({'token': token}, 201)
        else:
            return error_response('Server error while signing up user, please try again later', 500)
