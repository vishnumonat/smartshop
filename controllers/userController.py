import json
from flask import Blueprint, Response, request, jsonify
from extentions import socket
from flask_restplus import Resource
from repository.userRepository import UserRepository
from flask_socketio import emit, disconnect
from utils.rfidUtils import listen_for_rfid

repository = UserRepository()
users = Blueprint('users', __name__)

@users.route('/users')
def get():
	"""List all registered users"""
	users = repository.get_all_users()
	return Response(json.dumps([user for user in users]), mimetype="application/json", status=200)


@users.route('/users', methods=['POST'])
def add_user():
	body = request.json
	id = repository.insert_user(body)
	return jsonify(id), 200


@socket.on('scan_rfid')
def on_connect():
	print('scan_rfid sid', request.sid)
	print('scan_rfid socket reopened')
	rfid = listen_for_rfid()
	print(rfid)
	emit('scanned_rfid', {'rfid': rfid})