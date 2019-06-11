import enum

from app.models.base_model import BaseModel
from app.utils.db import db


class TypeEnum(enum.Enum):
    one_way = 'One Way'
    round_trip = 'Round Trip'


class Ticket(BaseModel):
    __tablename__ = 'ticket'

    flight_type = db.Column('flight_type', db.Enum(TypeEnum), nullable=False, default=TypeEnum.one_way)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'), nullable=False)
    flight_seat_id = db.Column(db.Integer, db.ForeignKey('flight_seats.id'), nullable=False)
    return_flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'), nullable=True)
    return_flight_seat_id = db.Column(db.Integer, db.ForeignKey('flight_seats.id'), nullable=True)
    ticket_code = db.Column(db.String(7), nullable=False)

    def serialize_items(self):
        """it triggers serialize method from sql_alchemy_bookmark_object."""
        return self.serialize()

    def __repr__(self):
        return '<Ticket {}>'.format(self.name)
