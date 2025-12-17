import yfinance as yf
import pandas as pd

# Get Opening Prices from a list of assets for a period of one year and return a Dataframe 
# Index = Ticker + Column = Asset => Price
def getTickers(list): 
    tickers = yf.Tickers(list)

    df = pd.DataFrame(tickers.history(period='1y'))["Open"]

    return df 



tickers = yf.Tickers('msft aapl goog')

print(getTickers('msft aapl goog'))