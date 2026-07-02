from flask import Blueprint, render_template, request
from ..src.backtest import backtest
from ..src.parameter import backtest_param


home = Blueprint('home', __name__)

@home.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		param = backtest_param(
		lot = float(request.form['lot']),
		risk_percent = float(request.form['risk']),
		contract_size = int(request.form['contract']),
		initial_balance = int(request.form['balance']),
		leverage = int(request.form['leverage']),
		fee_perlot = int(request.form['fee'])
		)

		result = backtest(param)

		print(result)

	return render_template(
		'index.html'
	)
