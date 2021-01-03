from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from database.models import SomeEntity, AnotherEntity, ThirdEntity  # noqa
    db.drop_all()
    db.create_all()
