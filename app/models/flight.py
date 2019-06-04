import enum

from app.models.base_model import BaseModel
from app.utils.db import db


class MyEnum(enum.Enum):
    cancelled = 'Cancelled'
    active = 'Active'
    unknown = 'Unknown'


class Flight(BaseModel):
    __tablename__ = 'flight'

    airline = db.Column(db.Integer, db.ForeignKey('airline.id'), nullable=False)
    departure_time = db.Column(db.Time, nullable=False)
    departure_date = db.Column(db.Date, nullable=False)
    arrival_time = db.Column(db.Time, nullable=False)
    departure_location = db.Column(db.String(50), nullable=False)
    arrival_location = db.Column(db.String(50), nullable=False)
    flight_code = db.Column(db.String(10), nullable=False, unique=True)
    no_of_seats = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column('status', db.Enum(MyEnum), nullable=False, default=MyEnum.unknown)
    seats = db.relationship('Flight_Seats', backref='flight', lazy=True)

    def serialize_items(self):
        """it triggers serialize method from sql_alchemy_bookmark_object."""
        return self.serialize()

    def __repr__(self):
        return '<Flight {}>'.format(self.name)
