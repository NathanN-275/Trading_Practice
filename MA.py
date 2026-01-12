# Moving average  
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# defining data frame -> smp500
df = yf.download('SPY')

print(df.head())

plt.plot(df['Close'])

# defining moving average
# #df['MA'] = df['Close'].rolling(3).mean() # 3-window moving average
df['MA'] = df['Close'].rolling(50).mean()
df

# plotting moving average and closing price
TICKER = 'SPY' 
WINDOW = 20 # global variable for moving average window size

df = yf.download(TICKER, period="max")
df['MA'] = df['Close'].rolling(WINDOW).mean()

# looking at smaller frames

plt.plot(df['Close']) # plotting the close price
plt.plot(df['MA']) # plotting moving average
plt.legend([f'{TICKER} Close Price', f'{WINDOW} Moving Average'])
plt.title(f'{TICKER} close vs moving average')

df.columns = df.columns.get_level_values(0)

def add_ma_strategy(df):
  df['Strategy'] = np.where(df['Close:'] > df['MA'], 1, -1)
  return df

df = add_ma_strategy(df)
df['asset_cumulative'] = np.cumprod(1 + df['Close'].pct_change()) - 1
df