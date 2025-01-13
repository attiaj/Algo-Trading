from pypm import metrics, signals, data_io, simulation
import pandas as pd
from typing import Tuple, List, Dict, Callable, NewType, Any

def simulate_portfolio():

    print("test change")
    bollinger_n = 20
    #sharpe_n = 100
    sharpe_n = 100
    #According to optimize_portfolio.py, the best results come with a bollinger_n of 20 and a sharpe_n of 80, so let's see the difference

    # Load in data (row = date, column = symbol)
    symbols: List[str] = data_io.get_all_symbols()
    prices: pd.DataFrame = data_io.load_eod_matrix(symbols)
    #print(prices)

    # Use the Bollinger Band outer band crossover as a signal
    _bollinger = signals.create_bollinger_band_signal
    signal = prices.apply(_bollinger, args=(bollinger_n,), axis=0)
    #print(signal)

    # Use a rolling sharpe ratio approximation as a preference matrix
    _sharpe = metrics.calculate_rolling_sharpe_ratio
    preference = prices.apply(_sharpe, args=(sharpe_n, ), axis=0)
    #print(preference)

    # Run the simulator
    simulator = simulation.SimpleSimulator(
        initial_cash=10000,
        max_active_positions=5,
        percent_slippage=0.0005,
        trade_fee=1,
    )
    simulator.simulate(prices, signal, preference)

    # Print results
    simulator.portfolio_history.print_position_summaries()
    simulator.print_initial_parameters()
    simulator.portfolio_history.print_summary()
    simulator.portfolio_history.plot()
    simulator.portfolio_history.plot_benchmark_comparison()

if __name__ == '__main__':
    simulate_portfolio()
