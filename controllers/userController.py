import json
from flask import Blueprint, Response, request, jsonify
from extentions import socket
from flask_restx  import Resource
from repository.userRepository import UserRepository
from flask_socketio import emit, disconnect
from utils.barcodeUtils import listen_for_barcode

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
	rfid = listen_for_barcode()
	print(rfid)
	emit('scanned_rfid', {'rfid': rfid})
	

@socket.on('scan_registered_rfid')
def on_connect():
	print('scan_registered_user sid', request.sid)
	print('scan_registered_user socket reopened')
	rfid = listen_for_barcode()
	user = repository.get_user_by_column('rfid', rfid)
	if(user != None):
		emit('scanned_registered_rfid', user)
	else:
		emit('scanned_registered_rfid', None)