from flask import request, g, jsonify
from flask_restful import Resource, Api

from app.models import Ticket
from app.utils.validator import Validator
from app.utils.tools import (
  success_response,
  error_response,
  serialize_ticket_list
)


class BookedResource(Resource):

    @Validator.validate_admin_token()
    @Validator.validate_flight_exists()
    def get(self, flight_id):
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

        booked_tickets = Ticket.query.filter_by(flight_id=flight_id, is_deleted=False).paginate(page, per_page, False)

        response = {
            'currentPage': booked_tickets.page,
            'pages': booked_tickets.pages,
            'pageSize': booked_tickets.per_page,
            'count': booked_tickets.total,
            'data': serialize_ticket_list(booked_tickets.items)
        }

        return success_response(response, 200)