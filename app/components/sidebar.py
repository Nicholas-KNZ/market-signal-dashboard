from dash  import html, dcc
import dash

def sidebar(pages):
    return html.Div([
        html.Button("Open"),
        html.H3(children="Portfolio Manager"),
        html.Div(
        [html.Div(dcc.Link(children=page["name"], href=page["path"]), className="side-bar-link") for page in pages], className="sidebar-links"
        ),
        
    ], className="sidebar")