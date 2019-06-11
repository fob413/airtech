from flask_mail import Message, Mail
from flask import render_template
from threading import Thread

from app import app


def send_async_email(apps, msg):
    from app import app

    with app.app_context():
        mail = Mail(app)
        mail.send(msg)
        

def send_email(subject, sender, recipients, flight, flight_seat, user, ticket):
    msg = Message(subject, sender=sender, recipients=[recipients])

    msg.html = render_template('flight_email.html', flight=flight, flight_seat=flight_seat, user=user, ticket=ticket)
    msg.body = render_template('flight_email.txt', flight=flight, flight_seat=flight_seat, user=user, ticket=ticket)

    Thread(target=send_async_email, args=(app, msg)).start()


def send_return_trip_email(subject, sender, recipients, flight, flight_seat, user, ticket, return_flight, return_flight_seat):
    msg = Message(subject, sender=sender, recipients=[recipients])

    msg.html = render_template('return_flight_email.html', flight=flight, flight_seat=flight_seat, user=user, ticket=ticket, return_flight=return_flight, return_flight_seat=return_flight_seat)
    msg.body = render_template('return_flight_email.txt', flight=flight, flight_seat=flight_seat, user=user, ticket=ticket, return_flight=return_flight, return_flight_seat=return_flight_seat)

    Thread(target=send_async_email, args=(app, msg)).start()
