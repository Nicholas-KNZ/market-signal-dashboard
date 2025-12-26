# Import packages
import dash 
from dash import Dash, html, dcc
from components import sidebar

# Initialize the app
app = Dash(use_pages=True)

# App layout
app.layout = html.Div(children=[
    sidebar.sidebar(dash.page_registry.values()),
    dash.page_container
], className="main-container")

# Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8050, debug=True) #  Set to false for Docker 
