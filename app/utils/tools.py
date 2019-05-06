import os
import datetime
import jwt

from flask import jsonify
from flask_bcrypt import Bcrypt

from app.models.airline import Airline


bcrypt = Bcrypt()

def error_response(error, error_status):
    response = jsonify({
        'error': error,
        'status': '{}'.format(error_status)
    })
    response.status_code = error_status
    return response


def success_response(data, status):
    response = jsonify({
        'status': status,
        'data': [data]
    })
    response.status_code = status
    return response


def generate_hash(password):
    return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")


def check_hash(hash_password, password):
    try:
        is_authenticated = bcrypt.check_password_hash(hash_password, password)
        return is_authenticated
    except:
        return False


def generate_token(user_id):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'user_id': user_id
    }

    return jwt.encode(
        payload,
        os.getenv('JWT_SECRET_KEY'),
        algorithm='HS256'
        ).decode("utf-8")


def generate_admin_token(user_id):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'user_id': user_id
    }

    return jwt.encode(
        payload,
        os.getenv('ADMIN_JWT_SECRET_KEY'),
        'HS256'
        ).decode("utf-8")


def get_airline(airline_id):
    airline = Airline.query.filter_by(id=airline_id).first()

    return airline


def duplicate_exists(item, possible_duplicates):
    if len(possible_duplicates) > 0:
        if possible_duplicates[0] != item:
            return True
        else:
            return False
    else:
        return False