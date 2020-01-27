from flask_mysqldb import MySQL
from flask_socketio import SocketIO

mysql = MySQL()

socket = SocketIO(cors_allowed_origins='*');
