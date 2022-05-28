import json

import requests

from flask import Response


def handle_response(response: object, status_code: int) -> Response:
    return Response(response=json.dumps(response), status=status_code, content_type='application/json')


def handle_request(url: str, body=None) -> Response:
    if url is None:
        return handle_response(response={'error': 'url is missing'}, status_code=400)

    if body is None:
        response: object = requests.get(url)
    else:
        response: object = requests.post(url, json=body)

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
