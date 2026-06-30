from flask import Blueprint

route = Blueprint('route', __name__)

@route.route('/dashboard')
def dashboard():
	return 'halo'