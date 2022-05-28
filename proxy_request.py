from flask import request, Response
from flask_restful import Resource

from response import handle_request


class ProxyRequest(Resource):
    def __init__(self: 'ProxyRequest'):
        pass

    def get(self: 'ProxyRequest') -> Response:
        url: str = request.args.get('url', type=str, default=None)
        response: Response = handle_request(url)
        return response

    def post(self: 'ProxyRequest') -> Response:
        url: str = request.form.get('url', type=str, default=None)
        body: object = request.get_json()
        response: Response = handle_request(url, body)
        return response
