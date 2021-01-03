import logging
import os

from flask import request, send_file
from flask_restplus import Resource
from api.some_service.business import create_some_entity, update_some_entity, delete_some_entity
from api.some_service.serializers import some_entity
from api.some_service.parsers import file_upload_parser, file_path_parser
from api.restplus import api
from database.models import SomeEntity

log = logging.getLogger(__name__)

ns = api.namespace('some_service/some_entity', description='Operations related to some entity')


@ns.route('/download/')
class DownloadFile(Resource):
    @api.expect(file_path_parser)
    def get(self):
        """
        Download file from server

        provide full path, like "/restplus_example/data.csv"
        """
        return send_file(open(request.args['file_path'], 'rb'),
                        mimetype='application/octet-stream',
                        as_attachment=True,
                        attachment_filename='{0}'.format(os.path.basename(request.args['file_path']))
        )


@ns.route('/upload/')
class Upload(Resource):
    @api.expect(file_upload_parser)
    def post(self):
        """
        Load file onto the server
        """
        if request.files['some_file'] == '':
            return 'No selected file', 400
        
        # save file into the root folder of the project        
        filename = 'data.csv'
        request.files['some_file'].save(filename)        
        #process_file(filename)

        return 'File has been processed successfully'


@ns.route('/')
class SomeEntityCollection(Resource):

    @api.marshal_list_with(some_entity)
    def get(self):
        """
        Returns list of some entities.
        """
        some_entities = SomeEntity.query.all()
        return some_entities

    @api.response(201, 'Some entity successfully created.')
    @api.expect(some_entity)
    def post(self):
        """
        Creates a new some entity.

        * Send a JSON object with new parameters in the request body.

        ```
        {
            "another_entity_id": 1,
            "field_dttm": "2021-01-02T20:42:15.042Z",
            "field_int": 15,
            "field_str": "some_string_value"
        }
        ```
        """
        data = request.json
        create_some_entity(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Some entity not found.')
class SomeEntityItem(Resource):

    @api.marshal_with(some_entity)
    def get(self, id):
        """
        Returns some entity.
        """
        return SomeEntity.query.filter(SomeEntity.id == id).one()

    @api.expect(some_entity)
    @api.response(204, 'Some entity successfully updated.')
    def put(self, id):
        """
        Updates some entity.

        * Send a JSON object with new parameters in the request body.

        ```
        {
            "another_entity_id": 1,
            "field_dttm": "2021-01-02T20:42:15.042Z",
            "field_int": 15,
            "field_str": "some_string_value"
        }
        ```

        * Specify the ID of the some entity to modify in the request URL path.
        """
        data = request.json
        update_some_entity(id, data)
        return None, 204

    @api.response(204, 'Some entity successfully deleted.')
    def delete(self, id):
        """
        Deletes some entity.
        """
        delete_some_entity(id)
        return None, 204
