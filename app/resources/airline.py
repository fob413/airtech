from flask_restful import Resource
from flask import request, g, jsonify

from app.models.airline import Airline
from app.models.user import User
from app.utils.validator import Validator
from app.utils.tools import (
    success_response,
    error_response,
    get_airline,
    duplicate_exists,
    serialize_list
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

    @Validator.validate_admin_token()
    def get(self):
        args = request.args
        
        if args.get('page'):
            try:
                page = int(args.get('page'))
            except:
                page = 0
        else:
            page = 0

        if args.get('limit'):
            try:
                per_page = int(args.get('limit'))
            except:
                per_page = 5
        else:
            per_page = 5

        airlines = Airline.query.paginate(page, per_page, False)

        response = {
            'currentPage': airlines.page,
            'pages': airlines.pages,
            'pageSize': airlines.per_page,
            'count': airlines.total,
            'data': serialize_list(airlines.items)
        }
        return success_response(response, 200)


class Single_Airline(Resource):

    @Validator.validate_admin_token()
    def get(self, airline_id):
        airline = get_airline(airline_id)

        if airline:
            response = airline.serialize()

            return success_response(response, 200)
        else:
            return error_response('This airline does not exist', 404)

    @Validator.validate_admin_token()
    @Validator.validate([
        'name|required:str',
        'nameAbb|required:str'
    ])
    def put(self, airline_id):
        airline = get_airline(airline_id)

        if airline:
            payload = request.get_json()
            
            name, nameAbb = payload['name'], payload['nameAbb']
            nameExists = Airline.query.filter_by(name=name).all()
            nameAbbExists = Airline.query.filter_by(name_abb=nameAbb).all()

            if duplicate_exists(airline, nameExists):
                return error_response('An airline already exist with the name', 400)

            if duplicate_exists(airline, nameAbbExists):
                return error_response('An airline already exist with the name abbreviation', 400)

            airline.name = payload['name']
            airline.name_abb = payload['nameAbb']
            airline.save()
            updated_airline = airline.serialize()

            return success_response(updated_airline, 200)
        else:
            return error_response('This airline does not exist', 404)

    @Validator.validate_admin_token()
    def delete(self, airline_id):
        airline = get_airline(airline_id)

        if airline:
            airline.is_deleted = True
            airline.save()

            return success_response({ "message": "Successfully deleted airline" }, 200)
        else:
            return error_response('This airline does not exist', 404)

        return error_response('successfullllllll', 200)
