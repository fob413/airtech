from app.models.base_model import BaseModel
from app.utils.db import db


class Airline(BaseModel):
    __tablename__ = 'airline'

    name = db.Column(db.String(120), nullable=False)
    name_abb = db.Column(db.String(10), nullable = False)

    def serialize_items(self):
        """it triggers serialize method from sql_alchemy_bookmark_object."""
        return self.serialize()

    def __repr__(self):
        return '<Airline {}>'.format(self.name)