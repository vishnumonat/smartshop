from mysql.connector import Error
from model.item import Item
from repository import connection

class ItemRepository:

	def __init__(self):
		self.connection = connection
		self.cursor = connection.cursor()

	def get_all_items(self):
		try:
			items = []
			self.cursor.execute("SELECT * from items")
			results = self.cursor.fetchall()
			for result in results:
				items.append(Item(result[0], result[1], result[2], result[3], result[4]))
			return items
		except Error as e:
			print('Sql connection Error: {}'.format(e))
			return null

	def get_item_by_column(self, column_name, value):
		try:
			query = "SELECT * from items WHERE {}=\'{}\'".format(column_name, value)
			self.cursor.execute(query)
			result = self.cursor.fetchone()
			return Item(result[0], result[1], result[2], result[3], result[4])
		except Error as e:
			print('Sql connection Error: {}'.format(e))
			return null


	def insert_item(self, item):
		try:
			query = "Insert into items (barcodeid, name, price, weight) values (%s, %s, %s, %s)"
			self.cursor.execute(query, (item['barcodeid'], item['name'], item['price'], item['weight']))
			connection.commit()
			return self.cursor.lastrowid
		except Error as e:
			print('Sql connection Error: {}'.format(e))
			return null

