'''
from dbConnector import *
from repository.itemRepository import ItemRepository

def main():
	connection = make_connection("localhost", "smartshop", "root", "raspberrypi" )
	itemRepository = ItemRepository(connection)
	print(list(map(str, itemRepository.get_all_items())))
	#print(str(userRepository.get_user_by_column("name", "junaid")))
	close_connection(connection)

if __name__ ==  '__main__':
	main()
'''
import os
from flask_restplus import Api
from flask import Blueprint
from flask import Flask
from flask_script import Manager
from flask_bcrypt import Bcrypt

from controllers.userController import users  as user_controller
from controllers.itemController import items  as item_controller

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    flask_bcrypt.init_app(app)

    return app


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False

flask_bcrypt = Bcrypt()
app = create_app(Config())
app.register_blueprint(user_controller)
app.register_blueprint(item_controller)

app.app_context().push()

manager = Manager(app)

@manager.command
def run():
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    manager.run()
