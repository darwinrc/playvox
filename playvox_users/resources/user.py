import json
from flask import request
from flask_restful import Resource, abort, marshal_with, fields, reqparse

from models import UserModel
from .utils import get_payload_data

import logging

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
    '''TODO.'''
    def __init__(self):
        self.user_model = UserModel()

    @marshal_with(user_fields)
    def get(self):
        """Returns the list of users.
        
        Supports query string with filters for each user field"""
        args = request.args
        if not args:
            return self.user_model.get_all_users()
            
        logging.warn('ARGS')
        logging.warn(args['query'])
        
        # if args['query']:
        #     logging.warn(args['query'])
        #     #return self.user_model.get_all_users({})
                
        # return self.user_model.get_all_users(json.loads(args['query']))
        return self.user_model.get_all_users(json.loads(args['query']))

    
    @marshal_with(user_fields)
    def post(self):
        """Creates a new user."""
        data = get_payload_data()
        user = self.user_model.get_user_by_name(data['first_name'], data['last_name'])
        if user:
            abort(400, message='User with that name exists')

        return self.user_model.insert_user(data), 201


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
        
        data = get_payload_data()
        user = self.user_model.get_user_by_name(data['first_name'], data['last_name'])
        if user and str(user['_id']) != user_id:
            abort(400, message='User with that name exists')

        return self.user_model.update_user(user_id, data)
    
    def delete(self, user_id):
        """Removes the user identified by user_id."""
        user = self.user_model.get_user(user_id)
        if not user:
            abort(404, message='User does not exists')
        
        self.user_model.delete_user(user_id)
        
        return {'message':'succesfully deleted the user.'}
    
    
