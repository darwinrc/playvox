from flask import request

def get_payload_data():
    payload = request.get_json()
    
    return {
        'title': payload['title'],
        'body': payload['body'],
        'note_date': payload['note_date']
    }
