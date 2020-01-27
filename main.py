import os
from flask_restplus import Api
from flask import Blueprint
from flask import Flask
from flask_script import Manager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from extentions import mysql, socket

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    flask_bcrypt.init_app(app)
    mysql.init_app(app)
    socket.init_app(app)
    return app

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False

#from dbConnector import *
#connection = make_connection("localhost", "smartshop", "root", "raspberrypi" )
flask_bcrypt = Bcrypt()
app = create_app(Config())
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'smartshop'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'raspberrypi'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

from controllers.userController import users  as user_controller
from controllers.itemController import items  as item_controller
app.register_blueprint(user_controller)
app.register_blueprint(item_controller)

app.app_context().push()

CORS(app, resources=r'*')

manager = Manager(app)

@manager.command
def run():
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    manager.run()
