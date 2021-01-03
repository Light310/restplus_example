import logging
import os

from flask import request, send_file
from flask_restplus import Resource
from api.some_service.business import create_another_entity, update_another_entity, delete_another_entity
from api.some_service.serializers import another_entity
from api.some_service.parsers import file_upload_parser, file_path_parser
from api.restplus import api
from database.models import AnotherEntity

log = logging.getLogger(__name__)

ns = api.namespace('some_service/another_entity', description='Operations related to another entity')


@ns.route('/')
class AnotherEntityCollection(Resource):

    @api.marshal_list_with(another_entity)
    def get(self):
        """
        Returns list of another entities.
        """
        another_entities = AnotherEntity.query.all()
        return another_entities

    @api.response(201, 'Another entity successfully created.')
    @api.expect(another_entity)
    def post(self):
        """
        Creates a new another entity.

        * Send a JSON object with new parameters in the request body.

        ```
        {
          "name": "another_name"
        }
        ```
        """
        data = request.json
        create_another_entity(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Another entity not found.')
class AnotherEntityItem(Resource):

    @api.marshal_with(another_entity)
    def get(self, id):
        """
        Returns another entity.
        """
        return AnotherEntity.query.filter(AnotherEntity.id == id).one()

    @api.expect(another_entity)
    @api.response(204, 'Another entity successfully updated.')
    def put(self, id):
        """
        Updates another entity.

        * Send a JSON object with new parameters in the request body.

        ```
        {
          "name": "other_name"
        }
        ```

        * Specify the ID of another entity to modify in the request URL path.
        """
        data = request.json
        update_another_entity(id, data)
        return None, 204

    @api.response(204, 'Another entity successfully deleted.')
    def delete(self, id):
        """
        Deletes another entity.
        """
        delete_another_entity(id)
        return None, 204
