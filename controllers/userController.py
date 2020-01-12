import json
from flask import Blueprint, Response, request, jsonify
from flask_restplus import Resource
from repository.userRepository import UserRepository

repository = UserRepository()
users = Blueprint('users', __name__)

@users.route('/users')
def get():
	"""List all registered users"""
	users = repository.get_all_users()
	usersjson = list(map(lambda user: json.dumps(user.__dict__), users))
	return Response(usersjson, mimetype="application/json", status=200)


@users.route('/users', methods=['POST'])
def add_user():
	body = request.get_json()
	print(body)
	id = repository.insert_user(body)
	return jsonify(id), 200
