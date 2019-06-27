from flask import request

def get_payload_data():
    payload = request.get_json()
    
    return {
        'first_name': payload['first_name'],
        'last_name': payload['last_name'],
        'age': payload['age'],
        'gender': payload['gender'],
        'email': payload['email'],
        'registration_date': payload['registration_date']
    }