from flask import request

def get_payload_data():
    """Formats the user data for marshalling the response.
    
    Returns:
        The marshalled user
    """
    payload = request.get_json()
    
    return {
        'first_name': payload['first_name'],
        'last_name': payload['last_name'],
        'age': payload['age'],
        'sex': payload['sex'],
        'email': payload['email'],
        'registration_date': payload['registration_date']
    }
