import pandas as pd
import numpy as np
from pypm.indicators import calculate_macd_oscillator, \
    calculate_bollinger_bands, calculate_rsi
from pypm.data_io import load_eod_data


def create_macd_signal(series: pd.Series, n1: int, n2: int) -> pd.Series:
    """
    Create a momentum-based signal based on the MACD crossover principle. 
    Generate a buy signal when the MACD crosses above zero, and a sell signal when
    it crosses below zero.
    """

    # Calculate the macd and get the signs of the values.
    macd = calculate_macd_oscillator(series, n1, n2)
    macd_sign = np.sign(macd)

    # Create a copy shifted by some amount.
    macd_shifted_sign = macd_sign.shift(1, axis=0)

    # Multiply the sign by the boolean. This will have the effect of casting
    # the boolean to an integer (either 0 or 1) and then multiply by the sign
    # (either -1, 0 or 1).
    return macd_sign * (macd_sign != macd_shifted_sign)


def create_bollinger_band_signal(series: pd.Series, n: int=20) -> pd.Series:
    """
    Create a reversal-based signal based on the upper and lower bands of the 
    Bollinger bands. Generate a buy signal when the price is below the lower 
    band, and a sell signal when the price is above the upper band.
    """

    bollinger_bands = calculate_bollinger_bands(series, n)
    sell = series > bollinger_bands['upper']
    buy = series < bollinger_bands['lower']
    return (1*buy - 1*sell)

def create_bollinger_macd_signal(series: pd.Series, n: int=20, n1: int=5, n2: int=34) -> pd.Series:
    """
    Creates a combination of macd and bollinger signal, returning 1 or -1 ONLY when both signals
    return it, otherwise returning a 0. "If bollinger and macd signal both say to buy/sell, then do so,
    otherwise, do not do anything."
    """

    bollinger_bands = calculate_bollinger_bands(series, n)
    sell = series > bollinger_bands['upper']
    buy = series < bollinger_bands['lower']
    bollinger_signal = (1*buy - 1*sell)
    
    macd = calculate_macd_oscillator(series, n1, n2)
    macd_sign = np.sign(macd)
    macd_shifted_sign = macd_sign.shift(1, axis=0)
    macd_signal = macd_sign * (macd_sign != macd_shifted_sign)

    #lambda here to compare values within bollinger/macd series, and set them to 0
    #in the combination if they do not agree
    combined_signal = bollinger_signal.combine(macd_signal, lambda x, y: 0 if x!=y else x)
    return combined_signal

def create_rsi_sma_signal(series: pd.Series, n: int) -> pd.Series:
    """
    Creates a signal based on RSI - if RSI is a value of 20 or below, buy
    If RSI is a value of 80 or above, sell. This RSI is calculated based on SMA.
    """

    rsi_sma = calculate_rsi(series, lambda s: s.rolling(n).mean())
    rsi_signal = rsi_sma.apply(lambda x: -1 if x >= 80 else (1 if x <= 20 else 0))
    return rsi_signal

#def create_rsi_sma_signal(series:pd.Series, n: int=14):

if __name__ == '__main__':
    data = load_eod_data('AWU')
    closes = data['close']

    #sma = calculate_simple_moving_average(closes, 10)\
    macd_n1 = 5
    macd_n2 = 50
    macd = calculate_macd_oscillator(closes, macd_n1, macd_n2)
    macd_signal = create_macd_signal(closes, macd_n1, macd_n2)
    #macd.plot()
    #macd_signal.plot()

    bollinger_n = 20
    bollinger_bands = calculate_bollinger_bands(closes, bollinger_n)
    bollinger_bands = bollinger_bands.assign(closes=closes)
    bollinger_signal = create_bollinger_band_signal(closes, bollinger_n)
    #bollinger_bands.plot()
    #closes.plot()
    #bollinger_signal.plot()


    length = 14 #length of ema/sma/rma for rsi
    #rsi_ema = calculate_rsi(closes, lambda s: s.ewm(span=length).mean())
    rsi_sma = calculate_rsi(closes, lambda s: s.rolling(length).mean())
    #rsi_rma = calculate_rsi(closes, lambda s: s.ewm(alpha=1 / length).mean())  # Approximates TradingView.
    #rsi_sma.plot()

    rsi_sma_signal = create_rsi_sma_signal(closes, length)
    #rsi_sma_signal.plot()


    import matplotlib.pyplot as plt
    plt.show()