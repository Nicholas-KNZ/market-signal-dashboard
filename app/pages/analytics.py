from dash import Dash, html
import dash

dash.register_page(__name__, path="/analytics")

# Requires Dash 2.17.0 or later
layout = [html.Div(children= [

    html.H2(children="KPIs"),
    html.H3(children="Return"),
    html.H3(children="Volatility"),
    html.H3(children="Alpha Value"),
    html.H3(children="Beta Value")

])]


