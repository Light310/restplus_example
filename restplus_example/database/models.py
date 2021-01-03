# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from database import db

class SomeEntity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field_str = db.Column(db.String(80))
    field_int = db.Column(db.Integer)
    field_dttm = db.Column(db.DateTime)

    another_entity_id = db.Column(db.Integer, db.ForeignKey('another_entity.id'))
    another_entity = db.relationship('AnotherEntity', backref=db.backref('some_entity', lazy='dynamic'))

    def __init__(self, field_str, field_int, another_entity, field_dttm=None):
        self.field_str = field_str
        self.field_int = field_int
        if field_dttm is None:
            field_dttm = datetime.utcnow()
        self.field_dttm = field_dttm
        self.another_entity = another_entity

    def __repr__(self):
        return '<Some Entity %r>' % self.field_str


class AnotherEntity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Another Entity %r>' % self.name

class ThirdEntity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field1 = db.Column(db.Integer)
    field2 = db.Column(db.Integer)
    field3 = db.Column(db.Integer)

    def __init__(self):
        self.field1 = None
        self.field2 = None
        self.field3 = None

    def __repr__(self):
        return '<Third Entity %r>' % self.field1
