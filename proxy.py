import requests

from typing import Tuple

from flask import Flask, request
from flask_cors import CORS, cross_origin

app: Flask = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/')
def home() -> str:
    return "Hello!!"


def handle_request(url: str) -> Tuple[object, int]:
    print('given url:', url)
    if not url:
        return {'error': 'url is missing'}, 400

    response = requests.get(url)

    response_status_code = response.status_code

    if response_status_code != 200:
        return {
            'message': f'Expected response of url to be 200. Got {response_status_code}',
        }, 400

    try:
        return response.json(), 200
    except Exception as error:
        return {
            'message': f'could not parse json {response.text}',
            'error': str(error),
        }, 400


@app.route('/proxy', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_response() -> Tuple[object, int]:
    url: str = request.args.get('url', type=str, default=None)
    response: Tuple[object, int] = handle_request(url)
    return response


@app.route('/proxy/<string:url>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_response_with_url(url: str) -> Tuple[object, int]:
    response = handle_request(url)
    return response


app.run(host='0.0.0.0', port=8000)
