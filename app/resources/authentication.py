from flask_restful import Resource
from flask import request

from app.models.user import User
from app.utils.validator import Validator
from app.utils.tools import (
    generate_hash,
    error_response,
    generate_token,
    success_response,
    check_hash,
    generate_admin_token
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


class Signin(Resource):
    """
    Signin a user
    """

    @Validator.validate([
        'email|required:str',
        'password|required:str'
    ])
    def post(self):
        payload = request.get_json()

        user = User.query.filter_by(email=payload['email']).first()

        if not user:
            return error_response('Incorrect Email or password', 400)
        else:
            is_authenticated = check_hash(user.password, payload['password'])

            if is_authenticated:
                if user.is_admin:
                    token = generate_admin_token(user.id)

                    return success_response({'token': token}, 200)
                else:
                    token = generate_token(user.id)

                    return success_response({'token': token}, 200)
            else:
                return error_response('Incorrect Email or password', 400)
