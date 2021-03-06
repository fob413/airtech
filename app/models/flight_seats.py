from app.models.base_model import BaseModel
from app.utils.db import db


class Flight_Seats(BaseModel):
    __tablename__ = "flight_seats"

    flight_code = db.Column(db.String, db.ForeignKey('flight.flight_code'), nullable=False)
    seat = db.Column(db.String(3), nullable=False)
    is_available = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    tickets = db.relationship('Ticket', backref='flight_seats', lazy=True, foreign_keys='Ticket.flight_seat_id')
    return_tickets = db.relationship('Ticket', backref='return_flight_seats', lazy=True, foreign_keys='Ticket.return_flight_seat_id')

    def serialize_items(self):
        """it triggers serialize method from sql_alchemy_bookmark_object."""
        return self.serialize()

    def __repr__(self):
        return '<Flight_Seat {}>'.format(self.name)