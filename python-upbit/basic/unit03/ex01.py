import pyupbit
import pandas as pd


def resample(freq='3T'):
    df = pyupbit.get_ohlcv("KRW-BTC", "minute1")
    df1 = df['open'].resample(freq).first()
    df2 = df['high'].resample(freq).max()
    df3 = df['low'].resample(freq).min()
    df4 = df['close'].resample(freq).last()
    df5 = df['volume'].resample(freq).sum()

    df = pd.concat([df1, df2, df3, df4, df5], axis=1)
    return df

if __name__ == "__main__":
    df = resample('2T')
    print(df)