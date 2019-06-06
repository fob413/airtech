import os
import datetime
import jwt
import time
import uuid

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

def serialize_list(item_lists):
    result = []

    for item in item_lists:
        result.append(item.serialize())

    return result

def is_time_valid(time_input):
    try:
        time.strptime(time_input, '%H:%M')
        return True
    except ValueError:
        return False

def is_date_valid(date_input):
    try:
        datetime.datetime.strptime(date_input, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def generate_flight_code():
    return uuid.uuid4().hex[:10].upper()

def generate_seat_numbers(no_of_seats):
    seat_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    seat_index = 0
    seat_list = []
  
    for num in range(no_of_seats):
        seat_list.append(seat_letters[seat_index] + str(num + 1))

        if seat_index is (len(seat_letters) - 1): seat_index = 0
        else: seat_index += 1

    return seat_list

def validate_status(status):
    possible_status = ['ACTIVE', 'CANCELLED', 'UNKNOWN']

    if status.upper() in possible_status: return status.lower()
    else: return 'unknown'

def validate_flight_type(status):
    possible_status = ['ONE_WAY', 'ROUND_TRIP']

    if status.upper() in possible_status: return status.lower()
    else: return 'one_way'