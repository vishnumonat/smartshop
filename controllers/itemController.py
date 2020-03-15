import json
from flask import Blueprint, Response, request, jsonify
from extentions import socket
from flask_restplus import Resource
from repository.itemRepository import ItemRepository
from flask_socketio import emit
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
	id = repository.insert_item(body)
	return jsonify(id), 200


@socket.on('scan_barcode')
def on_connect():
	print('user connected')
	barcode = listen_for_barcode()
	print(barcode)
	emit('scanned_barcode', {'barcode': barcode}, broadcast=True)

@socket.on('scan_item')
def on_connect():
	print('user connected')
	barcode = listen_for_barcode()
	print(barcode)
	emit('scanned_item', repository.get_item_by_column('barcodeid', barcode), broadcast=True)
