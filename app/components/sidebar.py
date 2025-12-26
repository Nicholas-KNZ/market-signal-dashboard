from dash  import html, dcc
import dash

def sidebar(pages):
    return html.Div([
        html.Div([
            html.Button("☰", className="sidebar-button"),
            html.H3(children="Portfolio Manager")
        ], className="sidebar-header"),
       
        html.Div(
        [html.Div(dcc.Link(children=page["name"], href=page["path"]), className="sidebar-link") for page in pages], className="sidebar-links"
        ),
        
    ], className="sidebar")