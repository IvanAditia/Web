import pandas as pd
import numpy as np
from .feature.indicator import ema, standar_deviation
from ..config import PATH

def backtest():

	df = pd.read_parquet(PATH['gold_h1'])

	

	return df
