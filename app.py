from backend import create_app
from backend.api.websocket import socketio 

app = create_app()

if __name__ == '__main__':
	socketio.run(app, debug=True)