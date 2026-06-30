import pandas as pd
import numpy as np

def backtest(path):

	df = pd.read_parquet(path)

	print(df.columns)

	return df