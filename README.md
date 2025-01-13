# Algo-Trading

Program for algorithmic trading, with :

Code for various performance metrics, such as (Annualized) Volatility, Sharpe Ratio, Sortino Ratio, Calmar Ratio, Pure Profit Score, and Jensen's Alpha: /src/pypm/metrics.py

Code for various technical indicators, such as SMA, MACD, Bollinger Bands, and Chaikin Money Flow (more to be added): /src/pypm/indicators.py

Code which creates trading signals based on the above indicators: /src/pypm/signals.py

Classes to simulate an active/closed position on a given asset, and a portfolio with a list of said positions, to record performance over a period of time: /src/pypm/portfolio.py

Class for the simulator itself, simulating (only long) positions, buying and selling based on generated signals while recording results in its PorfolioHistory: /src/pypm/simulation.py

Much of the code currently used is sourced from Chris Conlan's Algorithmic Trading with Python (https://github.com/chrisconlan/algorithmic-trading-with-python) - his instructions on the code and math involved are detailed in his book of the same name.
