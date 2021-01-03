from flask_restplus import reqparse
from werkzeug.datastructures import FileStorage

file_upload_parser = reqparse.RequestParser()
file_upload_parser.add_argument('some_file', type=FileStorage, location='files')

file_path_parser = reqparse.RequestParser()
file_path_parser.add_argument('file_path', type=str, required=True)

third_entity_filter_parser = reqparse.RequestParser()
third_entity_filter_parser.add_argument('field1', type=str, location='args', help='field1', store_missing=False)
third_entity_filter_parser.add_argument('field2', type=str, location='args', help='field2', store_missing=False)
third_entity_filter_parser.add_argument('field3', type=str, location='args', help='field3', store_missing=False)
