from flask import request
from flask_restful import Resource
from app.models import Flight_Seats
from sqlalchemy import and_

from app.utils.validator import Validator
from app.utils.tools import (
    success_response,
    error_response,
    serialize_list
)


class FlightSeat(Resource):

    @Validator.validate_token()
    def get(self, flight_code):
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

        flight_seats = Flight_Seats.query.filter(
            and_(
                Flight_Seats.flight_code == flight_code,
                Flight_Seats.is_available is not False
            )
        ).paginate(page, per_page, False)

        response = {
            'currentPage': flight_seats.page,
            'pages': flight_seats.pages,
            'pageSize': flight_seats.per_page,
            'count': flight_seats.total,
            'data': serialize_list(flight_seats.items)
        }

        return success_response(response, 200)