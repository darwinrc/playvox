import os

from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)


class UserModel(object):
    '''TODO.'''
    def __init__(self):
        self.collection = client.playvox_users_collection

    def get_all_users(self):
        '''Returns all the users in the collection.'''
        return [u for u in self.collection.users.find()]
    
    def get_user(self, user_id):
        '''Returns a single user from the collection.'''
        return self.collection.users.find_one({'_id': ObjectId(user_id)})
    
    def get_user_by_name(self, first_name, last_name):
        '''Returns a single user from the collection given their first and last names.'''
        return self.collection.users.find_one({'first_name': first_name, 'last_name': last_name})

    def insert_user(self, new_user):
        '''Inserts a user in the collection.'''
        inserted_user = self.collection.users.insert_one(new_user)
        
        return self.collection.users.find_one({'_id': ObjectId(inserted_user.inserted_id)})

    def update_user(self, user_id, edited_user):
        '''Updates a user from the collection.'''
        self.collection.users.find_one_and_update({'_id': ObjectId(user_id)}, {"$set": edited_user})
        
        return self.collection.users.find_one({'_id': ObjectId(user_id)})

    def delete_user(self, user_id):
        '''Deletes a user from the collection.'''
        self.collection.users.delete_one({'_id': ObjectId(user_id)})
