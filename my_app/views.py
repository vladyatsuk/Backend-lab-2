from my_app import app
from flask import request
from datetime import datetime
import uuid

users = {}
categories = {}
records = {}

@app.route('/healthcheck')
def healthcheck():
    current_time = datetime.now().isoformat()
    status = 'OK'

    response_data = {
        'status': status,
        'timestamp': current_time
    }

    return response_data, 200

@app.get('/user/<user_id>')
def user_get(user_id):
    if user_id not in users:
        return {'error': f'No user found with id {user_id}'}, 404
    else:
        return users[user_id]

@app.delete('/user/<user_id>')
def user_delete(user_id):
    if user_id not in users:
        return {'error': f'No user found with id {user_id}'}, 404
    else:
        del users[user_id]
        return {'message': f'User {user_id} deleted successfully'}

@app.post('/user')
def user_add():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        name = request.json['name']
    else:
        name = request.args.get('name') 
    if not name:
        return {'error': 'Name is required'}, 400
    id = uuid.uuid4().hex
    user = {'id': id, 'name': name}
    users[id] = user
    return user

@app.get('/users')
def users_get():
    return list(users.values())
