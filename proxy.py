import requests

from flask import Flask, request
from flask import Response
from flask_cors import CORS, cross_origin

app: Flask = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/')
def home() -> str:
    return "Hello!!"


def handle_request(url: str) -> Response:
    if url is None:
        return Response(response={'error': 'url is missing'}, status=400)

    response = requests.get(url)

    response_status_code = response.status_code

    if response_status_code != 200:
        return Response(
            response={
                'message': f'Expected response of url to be 200. Got {response_status_code}'
            },
            status=400
        )

    try:
        return Response(response=response.json(), status=200)
    except Exception as error:
        return Response(
            response={
                'message': f'could not parse json {response.text}',
                'error': str(error)
            },
            status=400
        )


@app.route('/', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_response():
    url: str = request.args.get('url', type=str, default=None)
    return handle_request(url)


@app.route('/<string:url>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_response_with_url(url: str):
    return handle_request(url)


app.run(host='0.0.0.0', port=8000)
