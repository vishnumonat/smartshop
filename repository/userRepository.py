from mysql.connector import Error
from model.user import User
from extentions import mysql

class UserRepository:

	def get_all_users(self):
		try:
			cursor = mysql.connection.cursor()
			cursor.execute("SELECT * from users")
			results = cursor.fetchall()
			return results
		except Error as e:
			print('Sql connection Error: {}'.format(e))
			return null

	def get_user_by_column(self, column_name, value):
		try:
			cursor = mysql.connection.cursor()
			query = "SELECT * from users WHERE {}=\'{}\'".format(column_name, value)
			cursor.execute(query)
			result = cursor.fetchone()
			return User(result[0], result[1], result[2], result[3])
		except Error as e:
			print('Sql connection Error: {}'.format(e))
			return null

	def insert_user(self, user):
		try:
			connection = mysql.connection
			cursor = connection.cursor()
			query = "Insert into users (name, idnumber, rfid, is_admin) values (%s, %s, %s, False)"
			cursor.execute(query, (user['name'], user['idnumber'], user['rfid']))
			connection.commit()
			return cursor.lastrowid
		except Error as e:
			print('Sql connection Error: {}'.format(e))
			return null
