import pandas as pd
import numpy as np
from .feature.indicator import ema, standar_deviation
from ..config import PATH

def backtest():

	df = pd.read_parquet(PATH['gold'])

	initial_balance = 100
	lot = 0.01
	contract_size = 100
	fee_perlot = 6
	leverage = 500
	lot = 0.01
	balance = initial_balance
	trades = []
	equity_curve = []
	position = None

	df = ema(df, 25, 'close')
	df = ema(df, 50, 'close')
	df = standar_deviation(df, 50, 'close')

	

	return df
