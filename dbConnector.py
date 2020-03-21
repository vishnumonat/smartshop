import mysql.connector
from mysql.connector import Error

def make_connection(host, database, user, password):
	try:
		connection = mysql.connector.connect(host=host,
						    database = database,
						    user = user,
						    password = password)
		if(connection.is_connected()):
			db_info = connection.get_server_info()
			print("Connected to server", db_info)
		
		return connection
	except Error as  e:
		print("Error connecting to server", e)

def close_connection(connection):
	if(connection.is_connected()):
		connection.close()
		print("Mysql connection closed")





