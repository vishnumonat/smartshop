import json
from flask import Blueprint, Response, request
from flask_restplus import Resource
from repository.itemRepository import ItemRepository

repository = ItemRepository()
items = Blueprint('item', __name__)

@items.route('/items')
def get():
	"""List all registered items"""
	items = repository.get_all_items()
	itemsjson = list(map(lambda item: json.dumps(item.__dict__), items))
	return Response(itemsjson, mimetype="application/json", status=200)


@items.route('/items', methods=['POST'])
def add_item():
	body = request.get_json()
	id = repository.insert_item(body)
	return jsonify(id), 200
