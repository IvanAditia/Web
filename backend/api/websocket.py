from flask import Blueprint
from flask_socketio import SocketIO
import threading
import pandas as pd
from ..src.backtest import backtest 

websocket = Blueprint('websocket', __name__)
socketio = SocketIO()

@socketio.on('get_data')
def push_data():

	df = backtest()
	data = {
		'isi' : df.columns.tolist()
	}

	socketio.emit('market_data', data)

