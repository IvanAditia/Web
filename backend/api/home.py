from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/')
def index():

	text = 'terhubung'

	return render_template(
		'index.html',
		text = text
	)
