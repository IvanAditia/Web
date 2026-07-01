def kriteria_candle(df):
    df['candle'] = abs(df['close'] - df['open'])
    df['bull_candle'] = df['close'] > df['open']
    df['bear_candle'] = df['close'] < df['open']
    
    return
    