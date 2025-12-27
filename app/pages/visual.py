from dash import Dash, html
import dash

dash.register_page(__name__, path="/visuals")

# Requires Dash 2.17.0 or later
layout = [html.Div(children= [

    html.Div(className="glassCard")

])]


