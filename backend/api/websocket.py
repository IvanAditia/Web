from flask import Blueprint
from flask_socketio import SocketIO
import threading
import pandas as pd
from ..src.backtest import backtest 

websocket = Blueprint('websocket', __name__)
socketio = SocketIO()

@socketio.on('get_data')
def push_data():
		
	harga = {
		'isi' : 'test'
	}

	socketio.emit('market_data', harga)

