from flask_restful import Resource, marshal_with, fields

from models import NoteModel
from .utils import get_payload_data

note_fields = {
    '_id': fields.String,
    'user_id': fields.String,
    'title': fields.String,
    'body': fields.String,
    'note_date': fields.String
}

class Note(Resource):
    '''TODO.'''
    def __init__(self):
        self.note_model = NoteModel()

    @marshal_with(note_fields)
    def get(self, user_id):
        """Returns the list of notes for a user."""
        return self.note_model.get_user_notes(user_id) 
    
    @marshal_with(note_fields)
    def post(self, user_id):
        """Creates a new note for a user."""
        note = {
            'user_id': user_id
        }
        note.update(get_payload_data())
        
        return self.note_model.insert_note(note), 201
