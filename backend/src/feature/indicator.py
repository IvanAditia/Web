def ema(df, period, source='close'):
	df[f'ema_{period}'] = df[source].rolling(period).mean()
	return df

def standar_deviation(df, period, source='close'):
	df['sd'] = df[source].rolling(period).std()
	return df