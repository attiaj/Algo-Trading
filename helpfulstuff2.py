import pandas as pd
import datetime
from typing import List, Dict, Tuple, Any, NewType

#This one is helpful stuff from the ATiP Conlan book, snippets

#for more descriptiveness
v: List[Tuple[int, int, str]] = [(1, 2, 'a'), (4, 5, 'b')]

v: Dict[Tuple[int, int], List[str]] = {
    (2, 3): ['apple', 'banana'], 
    (4, 7): ['orange', 'pineapple']
}

StockTicker = NewType('StockTicker', str)
ticker: StockTicker = 'AAPL'

data = {
    'SPY' : {
        datetime.date(2000, 1, 4): 100,
        datetime.date(2000, 1, 5): 101,
    },
    'AAPL' : {
        datetime.date(2000, 1, 4): 300,
        datetime.date(2000, 1, 5): 303,
    },
}

df: pd.DataFrame = pd.DataFrame(data = data)
print(df)

#index by column
aapl_series: pd.Series = df['AAPL']
print(aapl_series)

#index by row
start_of_year_row: pd.Series = df.loc[datetime.date(2000, 1, 4)]
print(start_of_year_row)

#index by both
start_of_year_price: pd.Series = df['AAPL'][datetime.date(2000, 1, 4)]
print(start_of_year_price)

series = pd.Series(data = data['SPY'])
print(series)

