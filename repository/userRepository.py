from mysql.connector import Error
from model.user import User
from repository import connection

class UserRepository:

	def __init__(self):
		self.connection = connection
		self.cursor = connection.cursor()

	def get_all_users(self):
		try:
			users = []
			self.cursor.execute("SELECT * from users")
			results = self.cursor.fetchall()
			for result in results:
				users.append(User(result[0], result[1], result[2], result[3]))
			return users
		except Error as e:
			print('Sql connection Error: {}'.format(e))
			return null

	def get_user_by_column(self, column_name, value):
		try:
			query = "SELECT * from users WHERE {}=\'{}\'".format(column_name, value)
			self.cursor.execute(query)
			result = self.cursor.fetchone()
			return User(result[0], result[1], result[2], result[3])
		except Error as e:
			print('Sql connection Error: {}'.format(e))
			return null

	def insert_user(self, user):
		try:
			query = "Insert into users (name, idnumber, rfid, is_admin) values (%s, %s, %s, False)"
			self.cursor.execute(query, (user['name'], user['idnumber'], user['rfid']))
			connection.commit()
			return self.cursor.lastrowid
		except Error as e:
			print('Sql connection Error: {}'.format(e))
			return null
