from flask_restplus import fields
from api.restplus import api

some_entity = api.model('SomeEntity', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of SomeEntity'),
    'field_str': fields.String(required=True, description='field_str'),
    'field_int': fields.Integer(required=True, description='field_int'),
    'another_entity_id': fields.Integer(attribute='another_entity.id'),
    'another_entity': fields.String(attribute='another_entity.name'),
    'field_dttm': fields.DateTime,
})

another_entity = api.model('AnotherEntity', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of another entity'),
    'name': fields.String(required=True, description='Name'),
})

third_entity = api.model('ThirdEntity', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of third entity'),
    'field1': fields.Integer(required=False, description='field1'),
    'field2': fields.Integer(required=False, description='field2'),
    'field3': fields.Integer(required=False, description='field3'),
})
