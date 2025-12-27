import yfinance as yf 
import pandas as pd 

# User Input: List of Assets => Buy Date / Sell Date and Quantity 

transactions = pd.read_csv('app/data/portfolio1.csv')


def getAssets(assetList):
    dat = yf.Tickers(assetList)
    return dat.history(period='1y')


def transformAssetList(assetList):
    listString = ''
    for asset in assetList: 
        listString += asset
        listString += ' '
    return listString

def transformAssetstoDollar(value): 
    value = round(value, 2)
    return value

def getTotalValuesandProfit(df = pd.read_csv('app/data/portfolio1.csv')):
    assetList = df.groupby('Symbol')['Stückzahl'].sum()
    transformedAssetList = transformAssetList(assetList.index)
    assetData = getAssets(transformedAssetList)
    value = 0 
    value_old = 0 

    # Accumulate closing prices
    for asset in assetList.index: 
        value += assetData.loc[assetData.index[0], ("Close", asset)] * assetList[asset]
        value_old += assetData.loc[assetData.index[-1], ("Close", asset)] * assetList[asset]

    
    return transformAssetstoDollar(value), transformAssetstoDollar(value_old)

