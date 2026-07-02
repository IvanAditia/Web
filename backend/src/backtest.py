import pandas as pd
import numpy as np
from .feature.indicator import ema, standar_deviation
from ..config import PATH
from .feature.candle import kriteria_candle
import matplotlib.pyplot as plt
from .parameter import backtest_param

df = pd.read_parquet(PATH['src_data']/'XAUUSD_H1.parquet')
df['return'] = np.log(df['close'])

def backtest(param):
	return(
		param.lot,
		param.risk_percent,
		param.contract_size,
		param.initial_balance,
		param.leverage,
		param.fee_perlot
	)