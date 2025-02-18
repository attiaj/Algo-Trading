import datetime
from typing import Callable

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pypm.data_io import load_eod_data


def calculate_simple_moving_average(series: pd.Series, n: int=20) -> pd.Series:
    """Calculates the simple moving average"""
    return series.rolling(n).mean()


def calculate_simple_moving_sample_stdev(series: pd.Series, n: int=20) -> pd.Series:
    """Calculates the simple moving average"""
    return series.rolling(n).std()


def calculate_macd_oscillator(series: pd.Series,
    n1: int=5, n2: int=34) -> pd.Series:
    """
    Calculate the moving average convergence divergence oscillator, given a 
    short moving average of length n1 and a long moving average of length n2
    """
    assert n1 < n2, f'n1 must be less than n2'
    return calculate_simple_moving_average(series, n1) - \
        calculate_simple_moving_average(series, n2)


def calculate_bollinger_bands(series: pd.Series, n: int=20) -> pd.DataFrame:
    """
    Calculates the Bollinger Bands and returns them as a dataframe
    """

    sma = calculate_simple_moving_average(series, n)
    stdev = calculate_simple_moving_sample_stdev(series, n)

    return pd.DataFrame({
        'middle': sma,
        'upper': sma + 2 * stdev,
        'lower': sma - 2 * stdev
    })

def calculate_rsi(over: pd.Series, fn_roll: Callable) -> pd.Series:
    #https://stackoverflow.com/questions/20526414/relative-strength-index-in-python-pandas
    #https://www.investopedia.com/terms/r/rsi.asp

    # Get the difference in price from previous step
    delta = over.diff()
    # Get rid of the first row, which is NaN since it did not have a previous row to calculate the differences
    delta = delta[1:] 

    # Make the positive gains (up) and negative gains (down) Series
    up, down = delta.clip(lower=0), delta.clip(upper=0).abs()

    roll_up, roll_down = fn_roll(up), fn_roll(down)
    rs = roll_up / roll_down
    rsi = 100.0 - (100.0 / (1.0 + rs))

    # Avoid division-by-zero if `roll_down` is zero
    # This prevents inf and/or nan values.
    rsi[:] = np.select([roll_down == 0, roll_up == 0, True], [100, 0, rsi])
    # rsi = rsi.case_when([((roll_down == 0), 100), ((roll_up == 0), 0)])  # This alternative to np.select works only for pd.__version__ >= 2.2.0.
    rsi.name = 'rsi'

    # Assert range
    #valid_rsi = rsi[length - 1:]
    #assert ((0 <= valid_rsi) & (valid_rsi <= 100)).all()
    # Note: rsi[:length - 1] is excluded from above assertion because it is NaN for SMA.

    return rsi


def calculate_money_flow_volume_series(df: pd.DataFrame) -> pd.Series:
    """
    Calculates money flow series
    """
    mfv = df['volume'] * (2*df['close'] - df['high'] - df['low']) / \
                                    (df['high'] - df['low'])
    return mfv

def calculate_money_flow_volume(df: pd.DataFrame, n: int=20) -> pd.Series:
    """
    Calculates money flow volume, or q_t in our formula
    """
    return calculate_money_flow_volume_series(df).rolling(n).sum()

def calculate_chaikin_money_flow(df: pd.DataFrame, n: int=20) -> pd.Series:
    """
    Calculates the Chaikin money flow
    """
    return calculate_money_flow_volume(df, n) / df['volume'].rolling(n).sum()


if __name__ == '__main__':
    data = load_eod_data('AWU')
    closes = data['close']
    sma = calculate_simple_moving_average(closes, 10)
    macd = calculate_macd_oscillator(closes, 5, 50)

    bollinger_bands = calculate_bollinger_bands(closes, 100)
    bollinger_bands = bollinger_bands.assign(closes=closes)
    #bollinger_bands.plot()

    length = 14 #length of ema/sma/rma for rsi
    #rsi_ema = calculate_rsi(closes, lambda s: s.ewm(span=length).mean())
    rsi_sma = calculate_rsi(closes, lambda s: s.rolling(length).mean())
    #rsi_rma = calculate_rsi(closes, lambda s: s.ewm(alpha=1 / length).mean())  # Approximates TradingView.
    rsi_sma.plot()

    cmf = calculate_chaikin_money_flow(data)
    # cmf.plot()


    import matplotlib.pyplot as plt
    plt.show()