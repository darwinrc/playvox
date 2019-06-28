import os

from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)


class NoteModel(object):
    """Represents Note model from MongoDB and operates on it."""
    def __init__(self):
        self.collection = client.playvox_notes_collection

    def get_user_notes(self, user_id):
        '''Gets all the notes for a user.
        
        Args:
            user_id: A string representing the hash id for a user. 
        
        Returns:
            List of notes for the user
        '''
        return [u for u in self.collection.notes.find({'user_id': user_id})]

    def insert_note(self, new_note):
        '''Inserts a note in the collection.
        
        Args:
            new_note: A dict representing the note data to save.

        Returns:
           The data for the new note. 
        '''
        inserted_note = self.collection.notes.insert_one(new_note)
        
        return self.collection.notes.find_one({'_id': ObjectId(inserted_note.inserted_id)})
