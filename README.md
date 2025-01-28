# Algo-Trading

Program for algorithmic trading, with :

Code for various performance metrics, such as (Annualized) Volatility, Sharpe Ratio, Sortino Ratio, Calmar Ratio, Pure Profit Score, and Jensen's Alpha: /src/pypm/metrics.py

Code for various technical indicators, such as SMA, MACD, Bollinger Bands, and Chaikin Money Flow (more to be added): /src/pypm/indicators.py

Code which creates trading signals based on the above indicators: /src/pypm/signals.py

Classes to simulate an active/closed position on a given asset, and a portfolio with a list of said positions, to record performance over a period of time: /src/pypm/portfolio.py


Class for the simulator itself, simulating (only long) positions, buying and selling based on generated signals while recording results in its PorfolioHistory: /src/pypm/simulation.py

File with an example of a simulation run over a period of 10 years, iterated daily, with a simple signal based on only Bollinger Bands and a simple metric based on only Sharpe Ratio: /src/simulate_portfolio.py


Code for running multiple simulations, each with different values for indicators - to determine which combination of indicators and indicator-parameters yields the best results: /src/pypm/optimization.py

File with an example of an optimization run on only Bollinger Bands and Sharpe Ratio, where simulations are run on every possible combination of Bollinger n-value (n=SMA-period of middle band line) from [10, 20,..., 100], and Sharpe Benchmark Rate [10, 20,..., 100]. Determines which combination of Bollinger-n and Sharpe BR yields the best portfolio results. 



Much of the code currently used is sourced from Chris Conlan's Algorithmic Trading with Python - his instructions on the code and math involved are detailed in his book of the same name.
