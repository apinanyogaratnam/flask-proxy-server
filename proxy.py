import json

import requests

from flask import Flask, request, Response
from flask_cors import CORS, cross_origin

app: Flask = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/')
def home() -> str:
    return "Hello!!"


def handle_response(response: object, status_code: int) -> Response:
    return Response(response=json.dumps(response), status=status_code, content_type='application/json')


def handle_request(url: str) -> Response:
    if url is None:
        return handle_response(response={'error': 'url is missing'}, status_code=400)

    response = requests.get(url)

    response_status_code = response.status_code

    if response_status_code != 200:
        return handle_response(
            response={
                'message': f'Expected response of url to be 200. Got {response_status_code}'
            },
            status_code=400
        )

    try:
        return handle_response(response=response.json(), status_code=200)
    except Exception as error:
        return handle_response(
            response={
                'message': f'could not parse json {response.text}',
                'error': str(error)
            },
            status_code=400
        )


@app.route('/proxy', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_response() -> Response:
    url: str = request.args.get('url', type=str, default=None)
    response: Response = handle_request(url)
    return response


@app.route('/proxy/<string:url>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_response_with_url(url: str) -> Response:
    response: Response = handle_request(url)
    return response


app.run(host='0.0.0.0', port=8000)
