from app.models.base_model import BaseModel
from app.utils.db import db


class User(BaseModel):
    __tablename__ = 'user'

    firstname = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    tel = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    profile = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return '<User {}>'.format(self.firstname)
