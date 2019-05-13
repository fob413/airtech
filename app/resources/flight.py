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