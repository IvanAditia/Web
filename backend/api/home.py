from flask import Blueprint, render_template, request
from ..src.backtest import backtest
from ..src.parameter import backtest_param, data_parameter
import pandas as pd


home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def index():

	data_form = {
		'lot' : 0.01,
		'risk' : 0.01,
		'contract' : 100,
		'balance' : 20,
		'leverage' : 500,
		'fee' : 6
	}

	results = []
	

	return render_template(
		'index.html',
		lot = results[0]['lot'],
		risk = results[0]['risk_percent'],
		contract = results[0]['contract_size'],
		balance = results[0]['initial_balance'],
		leverage = results[0]['leverage'],
		fee = results[0]['fee_perlot'],
		form = data_form,
	)

@home.route('/backtest', methods=['POST'])