from dash  import html 
import yfinance

def valueCard(title, value):
    return html.Div([
        html.H3(children=title),
        html.H3(children=str(value) + " €")
    ], className="glass-card")