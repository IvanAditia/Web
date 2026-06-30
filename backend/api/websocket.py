from flask import Blueprint
from flask_socketio import SocketIO
import threading

websocket = Blueprint('websocket', __name__)
socketio = SocketIO()


@socketio.on('get_data')
def push_data():

	data = {
		'harga' : 'halo'
	}

	socketio.emit('market_data', data)

