from flask import Flask
from backend.api.websocket import socketio

def create_app():

	app = Flask(
		__name__,
		template_folder = '../frontend/templates',
		static_folder = '../frontend/static'
	)

	socketio.init_app(app)

	from backend.api.home import home
	from backend.api.route import route

	app.register_blueprint(home)
	app.register_blueprint(route)

	return app