# Import packages
import dash
from dash import Dash, html, dcc
import pandas as pd 
from logic import financeData
from components import transactionHistory

dash.register_page(__name__, path="/")

# Total Value 
df = pd.read_csv('app/data/portfolio1.csv')
total_value, old_value = financeData.getTotalValuesandProfit()
profit = round((total_value - old_value) / old_value, 2)

# App layout

layout = html.Div(children=[
    html.H2(children="Dashboard", className="dashboard-title"),

    # Card Row - 1 
    html.Div(className='cards-row', children = [
    # Portfolio Value Card 
        html.Div(
                className="glass-card",
                children=[
                    html.Div(
                        className="card-header",
                        children=[
                            html.H4("Portfolio Value"),
                            ],
                        ),

                    html.Div(
                        className="card-value",
                        children=[
                            html.Span("$", className="value"),
                            html.Span(total_value, className="value"),
                        ],
                    ),

                    html.Div(
                        className="card-footer",
                        children=[
                            html.Span(profit, className="profit positive"),
                            html.Span("%", className="percent"),
                            ],
                        ),
                    ],
            ), 
        html.Div(
                className="glass-card",
                children=[
                    html.Div(
                        className="card-header",
                        children=[
                            html.H4("Dividends"),
                            ],
                        ),

                    html.Div(
                        className="card-value",
                        children=[
                            html.Span("$", className="value"),
                            html.Span(total_value, className="value"),
                        ],
                    ),

                    html.Div(
                        className="card-footer",
                        children=[
                            html.Span(profit, className="profit positive"),
                            html.Span("%", className="percent"),
                            ],
                        ),
                    ],
            ),
        html.Div(
                className="glass-card",
                children=[
                    html.Div(
                        className="card-header",
                        children=[
                            html.H4("Dividends"),
                            ],
                        ),

                    html.Div(
                        className="card-value",
                        children=[
                            html.Span("$", className="value"),
                            html.Span(total_value, className="value"),
                        ],
                    ),

                    html.Div(
                        className="card-footer",
                        children=[
                            html.Span(profit, className="profit positive"),
                            html.Span("%", className="percent"),
                            ],
                        ),
                    ],
            ),
        html.Div(
                className="glass-card",
                children=[
                    html.Div(
                        className="card-header",
                        children=[
                            html.H4("Dividends"),
                            ],
                        ),

                    html.Div(
                        className="card-value",
                        children=[
                            html.Span("$", className="value"),
                            html.Span(total_value, className="value"),
                        ],
                    ),

                    html.Div(
                        className="card-footer",
                        children=[
                            html.Span(profit, className="profit positive"),
                            html.Span("%", className="percent"),
                            ],
                        ),
                    ],
            ),
        
    ]), 
    transactionHistory.chart(df)
])


'''
# Import packages
import dash
from dash import Dash, html, dcc
import plotly.express as px
import plotly.io as pio
import pandas as pd
import numpy as np 
from components import chart, value, transactionHistory









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
    html.H2(children="Dashboard", className="test"),
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
'''