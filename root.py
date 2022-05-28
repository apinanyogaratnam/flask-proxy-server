from flask import Response
from flask_restful import Resource

from response import handle_response


class Root(Resource):
    def __init__(self: 'Root') -> None:
        pass

    def get(self: 'Root') -> Response:
        return handle_response(response={'message': 'Api is running'}, status_code=200)
