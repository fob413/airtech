from flask import request, g, jsonify
from flask_restful import Resource, Api
from threading import Thread

from app.models.flight import MyEnum, Flight
from app.models.flight_seats import Flight_Seats
from app.utils.validator import Validator
from app.utils.tools import (
    success_response,
    error_response,
    generate_flight_code,
    validate_status,
    generate_seat_numbers
)


def create_flight_seat(flight_id, no_of_seats):
    from app import app

    with app.app_context():
        seats = generate_seat_numbers(no_of_seats)

        for seat_id in seats:
            new_seat = Flight_Seats(
                flight_id = flight_id,
                seat = seat_id,
                is_available = True
            )
            new_seat.save()


class FlightResource(Resource):

    @Validator.validate_admin_token()
    @Validator.validate([
        'airlineID|required:str',
        'departureTime|required:time',
        'departureDate|required:date',
        'noOfSeats|required:int',
        'arrivalTime|required:time',
        'price|required:float',
        'status|required:str',
        'departureLocation|required:str',
        'arrivalLocation|required:str'
    ])
    @Validator.validate_airline_exists()
    def post(self):
        payload = request.get_json()

        (airlineID, departureTime, departureDate, noOfSeats, arrivalTime,
        price, status, departureLocation, arrivalLocation ) = (payload['airlineID'],
        payload['departureTime'], payload['departureDate'], payload['noOfSeats'], payload['arrivalTime'],
        payload['price'], payload['status'], payload['departureLocation'], payload['arrivalLocation'])

        new_flight = Flight(
            airline = int(airlineID),
            departure_time = departureTime,
            departure_date = departureDate,
            arrival_time = arrivalTime,
            departure_location = departureLocation,
            arrival_location = arrivalLocation,
            flight_code = generate_flight_code(),
            no_of_seats = noOfSeats,
            price = float(price),
            status = validate_status(status)
        )
        new_flight.save()

        response = new_flight.serialize_items()

        # create flight seats
        Thread(target=create_flight_seat, args=(response['id'], new_flight.no_of_seats)).start()

        response['status'] = response['status'].value
        response['departureDate'] = response['departureDate'].strftime('%Y-%m-%d')
        response['departureTime'] = response['departureTime'].strftime('%H:%M')
        response['arrivalTime'] = response['arrivalTime'].strftime('%H:%M')
        return success_response(response, 201)


class Single_FlightResource(Resource):

    def get(self, flight_id):
        flight = Flight.query.filter_by(id=flight_id).first()

        if flight:
            response = flight.serialize_items()

            response['status'] = response['status'].value
            response['departureDate'] = response['departureDate'].strftime('%Y-%m-%d')
            response['departureTime'] = response['departureTime'].strftime('%H:%M')
            response['arrivalTime'] = response['arrivalTime'].strftime('%H:%M')
            return success_response(response, 200)
        else:
            return error_response('This flight does not exist', 404)

    @Validator.validate_admin_token()
    @Validator.validate([
        'airlineID|required:str',
        'departureTime|required:time',
        'departureDate|required:date',
        'noOfSeats|required:int',
        'arrivalTime|required:time',
        'price|required:float',
        'status|required:str',
        'departureLocation|required:str',
        'arrivalLocation|required:str'
    ])
    @Validator.validate_airline_exists()
    def put(self, flight_id):
        flight = Flight.query.filter_by(id=flight_id).first()

        if flight:
            payload = request.get_json()

            (airlineID, departureTime, departureDate, noOfSeats, arrivalTime,
            price, status, departureLocation, arrivalLocation ) = (payload['airlineID'],
            payload['departureTime'], payload['departureDate'], payload['noOfSeats'], payload['arrivalTime'],
            payload['price'], payload['status'], payload['departureLocation'], payload['arrivalLocation'])

            flight.airline = int(airlineID)
            flight.departure_date = departureDate
            flight.departure_time = departureTime
            flight.no_of_seats = noOfSeats
            flight.arrival_time = arrivalTime
            flight.price = float(price)
            flight.status = validate_status(status)
            flight.departure_location = departureLocation
            flight.arrival_location = arrivalLocation
            flight.save()

            response = flight.serialize_items()

            response['status'] = response['status'].value
            response['departureDate'] = response['departureDate'].strftime('%Y-%m-%d')
            response['departureTime'] = response['departureTime'].strftime('%H:%M')
            response['arrivalTime'] = response['arrivalTime'].strftime('%H:%M')
            return success_response(response, 200)
        else:
            return error_response('This Flight does not exist', 404)
