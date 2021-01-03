from database import db
from database.models import SomeEntity, AnotherEntity, ThirdEntity


def create_some_entity(data):
    field_str = data.get('field_str')
    field_int = data.get('field_int')
    another_entity_id = data.get('another_entity_id')
    another_entity = AnotherEntity.query.filter(AnotherEntity.id == another_entity_id).one()
    some_entity = SomeEntity(field_str, field_int, another_entity)
    db.session.add(some_entity)
    db.session.commit()


def update_some_entity(some_entity_id, data):
    some_entity = SomeEntity.query.filter(SomeEntity.id == some_entity_id).one()
    some_entity.field_str = data.get('field_str')
    some_entity.field_int = data.get('field_int')
    another_entity_id = data.get('another_entity_id')
    some_entity.another_entity = AnotherEntity.query.filter(AnotherEntity.id == another_entity_id).one()
    db.session.add(some_entity)
    db.session.commit()


def delete_some_entity(some_entity_id):
    some_entity = SomeEntity.query.filter(SomeEntity.id == some_entity_id).one()
    db.session.delete(some_entity)
    db.session.commit()


def create_another_entity(data):
    name = data.get('name')
    another_entity_id = data.get('id')

    another_entity = AnotherEntity(name)
    if another_entity_id:
        another_entity.id = another_entity_id

    db.session.add(another_entity)
    db.session.commit()


def update_another_entity(another_entity_id, data):
    another_entity = AnotherEntity.query.filter(AnotherEntity.id == another_entity_id).one()
    another_entity.name = data.get('name')
    db.session.add(another_entity)
    db.session.commit()


def delete_another_entity(another_entity_id):
    another_entity = AnotherEntity.query.filter(AnotherEntity.id == another_entity_id).one()
    db.session.delete(another_entity)
    db.session.commit()


def create_third_entity(data):
    third_entity = ThirdEntity()

    for k, v in data.items():
        setattr(third_entity, k, v)

    db.session.add(third_entity)
    db.session.commit()

def delete_third_entity(id):
    third_entity = ThirdEntity.query.filter(ThirdEntity.id == id).one()    
    db.session.delete(third_entity)
    db.session.commit()

def update_third_entity(id, data):
    third_entity = ThirdEntity.query.filter(ThirdEntity.id == id).one()

    for k, v in data.items():
        setattr(third_entity, k, v)

    db.session.add(third_entity)
    db.session.commit()