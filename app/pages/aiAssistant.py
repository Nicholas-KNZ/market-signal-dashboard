from dash import Dash, html
from components import transactionHistory
import pandas as pd 
import dash

dash.register_page(__name__, path="/ai")

# Requires Dash 2.17.0 or later
layout = [html.Div(children= [

    transactionHistory.chart(pd.read_csv('app/data/portfolio1.csv'))

])]

