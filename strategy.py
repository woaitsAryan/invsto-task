from model import HINDALCO
from db import Session, engine
import pandas as pd 
import numpy as np

session = Session()

query = session.query(HINDALCO)

df = pd.read_sql(query.statement, con=engine)

very_short_window = 5
short_window = 50
long_window = 200
df['short_mavg'] = df['close'].rolling(window=short_window, min_periods=1).mean()
df['long_mavg'] = df['close'].rolling(window=long_window, min_periods=1).mean()
df['very_short_mavg'] = df['close'].rolling(window=very_short_window, min_periods=1).mean()

# Create a column for the signals 
df['short_long_signal'] = 0.0
df['long_signal'] = 0.0
df['short_signal'] = 0.0
df['very_short_signal'] = 0.0
df.loc[short_window:, 'short_long_signal'] = np.where(df['short_mavg'][short_window:] > df['long_mavg'][short_window:], 1.0, 0.0)
df.loc[long_window:, 'long_signal'] = np.where(df['close'][long_window:] > df['long_mavg'][long_window:], 1.0, 0.0)
df.loc[short_window:, 'short_signal'] = np.where(df['close'][short_window:] > df['short_mavg'][short_window:], 1.0, 0.0)
df.loc[very_short_window:, 'very_short_signal'] = np.where(df['close'][very_short_window:] > df['very_short_mavg'][very_short_window:], 1.0, 0.0)

print(df['short_long_signal'])

df['short_long_positions'] = df['short_long_signal'].diff()
df['long_positions'] = df['long_signal'].diff()
df['short_positions'] = df['short_signal'].diff()
df['very_short_positions'] = df['very_short_signal'].diff()


def generate_report_short_long(capital):
    initial_capital = capital
    positions = df['short_long_positions']
    close = df['close']
    
    print(positions)
    print(close)

    stocks = positions.cumsum()
    cash = initial_capital - (positions * close).cumsum()

    portfolio_value = stocks * close + cash

    portfolio = pd.DataFrame(index=close.index)
    portfolio['total'] = portfolio_value

    portfolio['returns'] = portfolio['total'].pct_change()

    return portfolio

def generate_report_short(capital):
    initial_capital = capital
    positions = df['short_positions']
    close = df['close']
    signals = df['short_signal']
    portfolio = pd.DataFrame(index=close.index).fillna(0.0)
    portfolio['holdings'] = positions.multiply(close, axis=0)
    portfolio['cash'] = initial_capital - (positions.diff().multiply(close, axis=0)).cumsum()
    portfolio['total'] = portfolio['cash'] + portfolio['holdings']
    portfolio['returns'] = portfolio['total'].pct_change()
    return portfolio

def generate_report_long(capital):
    initial_capital = capital
    positions = df['long_positions']
    close = df['close']
    signals = df['long_signal']
    portfolio = pd.DataFrame(index=close.index).fillna(0.0)
    portfolio['holdings'] = positions.multiply(close, axis=0)
    portfolio['cash'] = initial_capital - (positions.diff().multiply(close, axis=0)).cumsum()
    portfolio['total'] = portfolio['cash'] + portfolio['holdings']
    portfolio['returns'] = portfolio['total'].pct_change()
    return portfolio

def generate_report_very_short(capital):
    initial_capital = capital
    positions = df['very_short_positions']
    close = df['close']
    signals = df['very_short_signal']
    portfolio = pd.DataFrame(index=close.index).fillna(0.0)
    portfolio['holdings'] = positions.multiply(close, axis=0)
    portfolio['cash'] = initial_capital - (positions.diff().multiply(close, axis=0)).cumsum()
    portfolio['total'] = portfolio['cash'] + portfolio['holdings']
    portfolio['returns'] = portfolio['total'].pct_change()
    return portfolio
    

session.close()