from datetime import date

import celery
from app.models import Flight, Flight_Seats
from app.models import Ticket
from app.utils.email import send_flight_reminder_email


@celery.task()
def send_remainder():
    from app import app

    with app.app_context():
        # get today's date
        today = date.today()

        # get tomorrow's flights
        flights = Flight.query.all()
        tomorrow_flights = []
        user_flight_tickets = []

        # print(today)
        for flight in flights:
            this = flight.serialize()
            diff = this['departureDate'] - today

            if diff.days == 1:
                tickets = flight.flight_tickets

                for ticket in tickets:
                    user_email = ticket.user.email
                    flight_serialize = flight
                    flight_seat = Flight_Seats.query.filter_by(id=ticket.flight_seat_id).first()
                    user = ticket.user
                    ticket_serialize = ticket

                    # send remainder email
                    send_flight_reminder_email('Flight Reminder',
                        'airtech@email.com',
                        user_email,
                        flight_serialize,
                        flight_seat,
                        user,
                        ticket_serialize)