import logging
import os

from flask import request, send_file
from flask_restplus import Resource
from api.some_service.business import create_third_entity, update_third_entity, delete_third_entity
from api.some_service.serializers import third_entity
from api.some_service.parsers import file_upload_parser, file_path_parser
from api.restplus import api
from database.models import ThirdEntity

log = logging.getLogger(__name__)

ns = api.namespace('some_service/third_entity', description='Operations related to third entity')


@ns.route('/')
class ThirdEntityCollection(Resource):

    @api.marshal_list_with(third_entity)
    def get(self):
        """
        Returns list of third entities.
        """
        third_entities = ThirdEntity.query.all()
        return third_entities

    @api.response(201, 'Third entity successfully created.')
    @api.expect(third_entity)
    def post(self):
        """
        Creates a new third entity.

        * Send a JSON object with new parameters in the request body.

        ```
        {
            "field1": 1,
            "field2": 2,
            "field3": 3
        }
        ```
        """
        data = request.json
        create_third_entity(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Third entity not found.')
class ThirdEntityItem(Resource):

    @api.marshal_with(third_entity)
    def get(self, id):
        """
        Returns third entity.
        """
        return ThirdEntity.query.filter(ThirdEntity.id == id).one()

    @api.expect(third_entity)
    @api.response(204, 'Third entity successfully updated.')
    def put(self, id):
        """
        Updates third entity.

        * Send a JSON object with new parameters in the request body.

        ```
        {
            "field1": 1,
            "field2": 2,
            "field3": 3
        }
        ```

        * Specify the ID of the third entity to modify in the request URL path.
        """
        data = request.json
        update_third_entity(id, data)
        return None, 204

    @api.response(204, 'Third entity successfully deleted.')
    def delete(self, id):
        """
        Deletes third entity.
        """
        delete_third_entity(id)
        return None, 204
