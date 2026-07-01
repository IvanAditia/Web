import pandas as pd
import numpy as np
from .feature.indicator import ema, standar_deviation
from ..config import PATH
from .feature.candle import kriteria_candle

def backtest():
    df = pd.read_parquet(PATH['gold_h1'])
    df['return'] = np.log(df['close'])
    return df