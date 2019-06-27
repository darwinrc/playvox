from flask_restful import Resource, abort, marshal_with, fields

from models import UserModel
from .utils import get_payload_data

user_fields = {
    '_id': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'age': fields.Integer,
    'gender': fields.String,
    'email': fields.String,
    'registration_date': fields.String
}

class User(Resource):
    '''TODO.'''
    def __init__(self):
        self.user_model = UserModel()

    @marshal_with(user_fields)
    def get(self):
        """Returns the list of users."""
        return self.user_model.get_all_users()
    
    @marshal_with(user_fields)
    def post(self):
        """Creates a new user."""
        return self.user_model.insert_user(get_payload_data()), 201


class SingleUser(Resource):
    '''TODO.'''
    def __init__(self):
        self.user_model = UserModel()

    @marshal_with(user_fields)
    def get(self, user_id):
        """Returns the user identified by user_id."""
        user = self.user_model.get_user(user_id)
        if not user:
            abort(404, message='User does not exists')

        return user
    
    @marshal_with(user_fields)
    def put(self, user_id):
        """Edits the user identified by user_id."""
        user = self.user_model.get_user(user_id)
        if not user:
            abort(404, message='User does not exists')

        return self.user_model.update_user(user_id, get_payload_data())
    
    def delete(self, user_id):
        """Removes the user identified by user_id."""
        user = self.user_model.get_user(user_id)
        if not user:
            abort(404, message='User does not exists')
        
        self.user_model.delete_user(user_id)
        
        return {'message':'succesfully deleted the user.'}
    
    