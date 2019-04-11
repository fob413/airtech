from app.utils.db import db
from datetime import datetime


def to_camel_case(snake_str):
    """Format string to camel case."""
    title_str = snake_str.title().replace("_", "")
    return title_str[0].lower() + title_str[1:]

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default = datetime.now())
    updated_at = db.Column(db.DateTime, default = datetime.now(), onupdate=datetime.now())
    is_deleted = db.Column(db.Boolean, default = False, nullable=False)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session().rollback()

    def serialize(self):
        """Map model objects to dict representation."""
        return {to_camel_case(column.name): getattr(self, column.name)
                for column in self.__table__.columns}
