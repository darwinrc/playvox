from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin

from resources import Note

app = Flask(__name__)
CORS(app)

api = Api(app)

api.add_resource(Note, '/v1/users/<user_id>/notes')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
