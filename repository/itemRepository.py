from mysql.connector import Error
from model.item import Item
from extentions import mysql

class ItemRepository:

	def __init__(self):
		self.connection = mysql.connection

	def get_all_items(self):
		try:
			cursor = mysql.connection.cursor()
			cursor.execute("SELECT * from items")
			results = cursor.fetchall()
			return results
		except Error as e:
			print('Sql connection Error: {}'.format(e))
			return null

	def get_item_by_column(self, column_name, value):
		try:
			query = "SELECT * from items WHERE {}=\'{}\'".format(column_name, value)
			cursor = mysql.connection.cursor()
			cursor.execute(query)
			result = cursor.fetchone()
			return result
		except Error as e:
			print('Sql connection Error: {}'.format(e))
			return null


	def insert_item(self, item):
		try:
			connection = mysql.connection
			cursor = connection.cursor()
			query = "Insert into items (barcodeid, name, price, weight) values (%s, %s, %s, %s)"
			cursor.execute(query, (item['barcodeid'], item['name'], item['price'], item['weight']))
			connection.commit()
			return cursor.lastrowid
		except Error as e:
			print('Sql connection Error: {}'.format(e))
			return null

