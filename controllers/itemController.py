import json
from flask import Blueprint, Response, request, jsonify
from extentions import socket
from flask_restplus import Resource
from repository.itemRepository import ItemRepository
from flask_socketio import emit, disconnect
from utils.barcodeUtils import listen_for_barcode

repository = ItemRepository()
items = Blueprint('item', __name__)

@items.route('/items')
def get():
	"""List all registered items"""
	items = repository.get_all_items()
	return Response(json.dumps([item for item in items]), mimetype="application/json", status=200)


@items.route('/items', methods=['POST'])
def add_item():
	body = request.json
	print(request.json)
	id = repository.insert_item(body)
	return jsonify(id), 200


@socket.on('scan_barcode')
def on_connect():
	print('scan_barcode sid', request.sid)
	print('scan_barcode socket reopened')
	barcode = listen_for_barcode()
	print(barcode)
	emit('scanned_barcode', {'barcode': barcode})

@socket.on('scan_item')
def on_connect():
	print('scan_item sid', request.sid)
	print('scan_item socket reopened')
	barcode = listen_for_barcode()
	print(barcode)
	item = repository.get_item_by_column('barcodeid', barcode)
	if(item != None):
		emit('scanned_item', item)


# @socket.on('disconnect')
# def test_disconnect():
# 	print('disconnect sid', request.sid)
# 	disconnect(request.sid.encode())
