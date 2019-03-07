import jwt
import os

from flask import request, make_response, jsonify, g
from functools import wraps
from validate_email import validate_email

from app.models.user import User
from app.utils.tools import error_response


class Validator:

    @staticmethod
    def validate(rules):
        """
        Validate request object
        based on rules set
        """

        def validate_request(f):
            
            @wraps(f)
            def decorated(*args, **kwargs):
                if not request.json:
                    return error_response('Request must be JSON formatted', 400)

                payload = request.get_json()

                if payload:
                    # loop through all validation rules
                    for rule in rules:
                        rule_array = rule.split('|')
                        request_key = rule_array[0]
                        validators = rule_array[1].split(':')

                        # if no request key or required is not part of validator
                        # continue the loop to avoid key errors.
                        if request_key not in payload and 'required' not in validators:
                            continue

                        # loop through all the validators specified
                        for validator in validators:

                            if (validator == 'required' and request_key not in payload) or payload[request_key] == '':
                                return error_response('{} is required'.format(request_key), 400)
                            
                            if (validator == 'str' and type(payload[request_key]) is not str) or (validator == 'str' and payload[request_key].strip() == ""):
                                return error_response('{} must be a valid string'.format(request_key), 400)

                            if validator == 'int' and type(payload[request_key]) is str and not payload[request_key].isdigit():
                                return error_response('Invalid {}'.format(request_key), 400)

                            if (request_key == 'email'):
                                is_valid_email = validate_email(payload[request_key])
                                if not is_valid_email:
                                    return error_response('Invalid {}'.format(request_key), 400)

                return f(*args, **kwargs)
            return decorated
        return validate_request

    @staticmethod
    def validate_user():
        """
        Validate no duplicate user exist
        """
        def user_exist(f):

            @wraps(f)
            def decorated(*args, **kwargs):
                payload = request.get_json()

                user = User.query.filter_by(email=payload['email']).first()

                if user:
                    return error_response('A user exists with {}'.format(payload['email']), 400)

                return f(*args, **kwargs)
            return decorated
        return user_exist

    @staticmethod
    def validate_token():
        """
        Validate user token
        """
        def token_validate(f):

            @wraps(f)
            def decorated(*args, **kwargs):

                # get authorization token
                authorization_token = request.headers.get('auth_token')
                if not authorization_token:
                    return error_response('User is not authenticated', 401)

                # decode token
                try:
                    payload = jwt.decode(
                        authorization_token,
                        os.getenv('JWT_SECRET_KEY'),
                        algorithm='HS256'
                    )
                except ValueError:
                    return error_response('User is not authenticated', 401)
                except jwt.ExpiredSignatureError:
                    return error_response('Authorization failed. Expired token.', 401)
                except jwt.DecodeError as error:
                    if str(error) == 'Signature verification failed':
                        return error_response('An error occured while decoding', 500)
                    else:
                        return error_response('Token provided is invalid', 401)

                g.user_id = payload['user_id']
                


                return f(*args, **kwargs)
            return decorated
        return token_validate

                

