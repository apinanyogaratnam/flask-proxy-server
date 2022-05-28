from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from proxy_request import ProxyRequest
from root import Root

app: Flask = Flask(__name__)
api: Api = Api(app)

CORS(app, support_credentials=True, resources={r"/*": {"origins": "*"}})

api.add_resource(Root, '/')
api.add_resource(ProxyRequest, '/proxy')

app.run(host='0.0.0.0', port=8000)
