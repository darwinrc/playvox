from flask import Flask
from flask_restful import Api
from resources import User, SingleUser

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/v1/users')
api.add_resource(SingleUser, '/v1/users/<user_id>')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
