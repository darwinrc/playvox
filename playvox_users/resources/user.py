import json
from flask import request
from flask_restful import Resource, abort, marshal_with, fields, reqparse

from models import UserModel
from .utils import get_payload_data

user_fields = {
    '_id': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'age': fields.Integer,
    'sex': fields.String,
    'email': fields.String,
    'registration_date': fields.String
}

class User(Resource):
    """Represents User resource in the API."""
    def __init__(self):
        self.user_model = UserModel()

    @marshal_with(user_fields)
    def get(self):
        """Gets the list of users.

        Supports query string with filters for each user field
  
        example:
            query={"first_name": "Margaret", "sex": "F"}

        Returns:
            A list of marshalled users according to the request filters
        """
        args = request.args
        if not args:
            return self.user_model.get_all_users()

        query = { k:v for k,v in json.loads(args['query']).items() if v }

        return self.user_model.get_all_users(query)

    @marshal_with(user_fields)
    def post(self):
        """Creates a new user.
        
        Returns:
            The newly created user or error if not found
        """
        data = get_payload_data()
        user = self.user_model.get_user_by_name(data['first_name'], data['last_name'])
        if user:
            abort(400, message='User with that name exists')

        return self.user_model.insert_user(data), 201


class SingleUser(Resource):
    """Represents a specific User resource in the API."""
    def __init__(self):
        self.user_model = UserModel()

    @marshal_with(user_fields)
    def get(self, user_id):
        """Gets the user identified by user_id.
        
        Returns:
            A marshalled user or an error if not found
        """
        user = self.user_model.get_user(user_id)
        if not user:
            abort(404, message='User does not exists')

        return user

    @marshal_with(user_fields)
    def put(self, user_id):
        """Edits the user identified by user_id.
        
        Args:
            user_id: A string identifying the hash id of a User.
    
        Returns:
            The updated marshalled user or an error if not found or duplicate
        """
        user = self.user_model.get_user(user_id)
        if not user:
            abort(404, message='User does not exists')

        data = get_payload_data()
        user = self.user_model.get_user_by_name(data['first_name'], data['last_name'])
        
        if user and str(user['_id']) != user_id:
            abort(400, message='User with that name exists')

        return self.user_model.update_user(user_id, data)

    def delete(self, user_id):
        """Removes the user identified by user_id.
        
        Args:
            user_id: A string identifying the hash id of a User.
    
        Returns:
            A message confirming the deletion
        """
        user = self.user_model.get_user(user_id)
        if not user:
            abort(404, message='User does not exists')

        self.user_model.delete_user(user_id)

        return {'message':'succesfully deleted the user.'}
