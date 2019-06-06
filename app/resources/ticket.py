from flask import request, g, jsonify
from flask_restful import Resource, Api
from threading import Thread
from app.models import Ticket, Flight_Seats, Flight

from app.utils.validator import Validator
from app.utils.tools import (
    success_response,
    error_response,
    validate_flight_type
)


def update_flight_seats(flight_type, seat_id, user_id, return_seat_id=None):
    from app import app

    with app.app_context():
        if flight_type.name == 'one_way':
            flight_seat = Flight_Seats.query.filter_by(id=seat_id).first()

            if flight_seat:
                flight_seat.is_available = False
                flight_seat.user_id = user_id

                flight_seat.save()
        else:
            flight_seat = Flight_Seats.query.filter_by(id=seat_id).first()

            if flight_seat:
                flight_seat.is_available = False
                flight_seat.user_id = user_id

                flight_seat.save()

            return_flight_seat = Flight_Seats.query.filter_by(id=return_seat_id).first()

            if return_flight_seat:
                return_flight_seat.is_available = False
                return_flight_seat.user_id = user_id

                return_flight_seat.save()



class TicketResource(Resource):

    @Validator.validate_token()
    @Validator.validate([
        'flightID|required:int',
        'flightSeatID|required:int',
        'flightType|required:str'
    ])
    @Validator.validate_flight_exists()
    @Validator.validate_flight_seat_exists()
    def post(self):
        payload = request.get_json()

        (flightID, flightSeatID, flightType) = (payload['flightID'], payload['flightSeatID'], payload['flightType'])
        flightType = validate_flight_type(flightType)

        if flightType =='round_trip':
            #validate return trip flight and flight_seat id are sent
            try:
                (returnFlightID, returnFlightSeatID) = (payload['returnFlightID'], payload['returnFlightSeatID'])
            except:
                return error_response('returnFlightID and returnFlightSeatID are requred for a round_trip', 400)

            # validate return trip flight exist
            return_flight = Flight.query.filter_by(id=returnFlightID).first()
            if not return_flight:
                return error_response('The return flight does not exist', 404)

            # validate return flight seat exists
            return_flight_seat = Flight_Seats.query.filter_by(id=returnFlightSeatID, is_available=True, flight_code=return_flight.flight_code).first()
            if not return_flight_seat:
                return error_response('The return flight seat does not exist', 404)

            # book flight ticket
            ticket = Ticket(
                flight_type = flightType,
                user_id = g.user_id,
                flight_id = flightID,
                flight_seat_id = flightSeatID,
                return_flight_id = returnFlightID,
                return_flight_seat_id = returnFlightSeatID
            )
            ticket.save()

            response = ticket.serialize()

            # update flight_seats
            Thread(target=update_flight_seats, args=(response['flightType'], response['flightSeatId'], response['userId'], response['returnFlightSeatId'])).start()

            response['flightType'] = response['flightType'].value
            return success_response(response, 201)

        else:
            ticket = Ticket(
                flight_type = flightType,
                user_id = g.user_id,
                flight_id = flightID,
                flight_seat_id = flightSeatID
            )
            ticket.save()

            response = ticket.serialize()

            # update flight_seats
            Thread(target=update_flight_seats, args=(response['flightType'], response['flightSeatId'], response['userId'], 5)).start()

            response['flightType'] = response['flightType'].value
            return success_response(response, 201)
