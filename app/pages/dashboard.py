# Import packages
from dash import Dash, html, dcc
import plotly.express as px
import plotly.io as pio
import pandas as pd
import numpy as np 
import dash
from components import chart, value, transactionHistory

dash.register_page(__name__, path="/")

# Color Theme 
pio.templates.default = "plotly_dark"

# Import Dummy Data 
df = pd.read_csv('app/data/portfolio1.csv')

# Calculate Portfolio Size 
portfolioValue = np.sum(df["Wert"])

# Create Asset Allocation Chart 
# Calcualte Allocation 

df_pie = pd.concat([df["Symbol"], df["Wert"] / np.sum(df["Wert"])], axis=1)

# Group by company
df_pie = df_pie.groupby(["Symbol"], as_index=False).sum()

# Create pie chart
fig = px.pie(df_pie, values='Wert', names='Symbol', title='Portfolio Pie Chart')

# App layout

layout = html.Div(children=[
    html.H1(children="Test", className="test"),
    html.Div(children = [
        value.valueCard("Portfolio Value", portfolioValue),
        value.valueCard("Dividends", portfolioValue)],className="dashboard-parent"),
     
    html.Div(children = [
        #chart.chart(df), 
        html.Div(dcc.Graph(
        id='portfolio-pie',
        figure=fig,
        className="glass-card"
    ), className="chart-card"), 
    ], className="dashboard-parent")
    ,
    transactionHistory.chart(pd.read_csv('app/data/portfolio1.csv'))
])
