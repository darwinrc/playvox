from flask import request

def get_payload_data():
    """Formats the note data for marshalling the response.
    
    Returns:
        The marshalled note
    """
    payload = request.get_json()
    
    return {
        'title': payload['title'],
        'body': payload['body'],
        'note_date': payload['note_date']
    }
