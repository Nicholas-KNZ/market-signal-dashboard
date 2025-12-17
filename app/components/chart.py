'''
from dash  import html, dcc
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime
import yfinance as yf

# Get Price Data for Assets
def getTickers(list): 
    tickers = yf.Tickers(list)

    df = pd.DataFrame(tickers.history(period='1y'))["Open"]

    return df 


# assetList: symbol => number 
# assetPrice: symbol => date => price
def getPortfolioValueonDay(assetList, assetPrices, date): 
    value = 0
    for asset in assetList.keys():
        value += assetList[asset] * assetPrices[asset][date]
    return value
    

def calculateChartDF(startDate, endDate, assetList={'msft': 10, "aapl": 100}: 
    assetPrice = None 
    dates = None 
    df = pd.DataFrame({'dates': dates, 'values': [getPortfolioValueonDay(assetList, assetPrice, date) for date in dates]})
    return df  


def chart(assetDf):
    endDate = datetime.now().strftime("%x")
    startDate = endDate 
    
    x,y = calculateChartDF(startDate, endDate)
    fig = go.Figure(data=[go.Scatter(x, y)])

    return html.Div([
        html.H3(children="ChartContainer"), 
        dcc.Graph(figure=fig)
    ], className="glass-card")




Asset DF

Symbol,Name,Stückzahl,Kaufkurs,Kaufdatum,Aktueller Kurs,Wert

<Wert Portfolio zu Tag 0> 

Kurse für jedes Symbol 
=> 

'''
