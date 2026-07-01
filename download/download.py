import MetaTrader5 as mt5
import pandas as pd

if not mt5.initialize():
	print('initialize gagal')

print('initialize berhasil')

symbol = 'XAUUSD.pc'

rates = mt5.copy_rates_from_pos(
	symbol,
	mt5.TIMEFRAME_H1,
	0,
	24405
)

df = pd.DataFrame(rates)

df['time'] = pd.to_datetime(df['time'], unit='s')

df.to_parquet('XAUUSD_H1.parquet')