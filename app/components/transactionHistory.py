from dash  import html 

def calculateChartDF(): 
    pass

def entry(transaction):
    return html.Div([
        html.Div(transaction["Name"], className="cell"),
        html.Div(transaction["Stückzahl"], className="cell"),
        html.Div(transaction["Kaufdatum"], className="cell"),
        html.Div("Kauf", className="cell")
    ], className="transaction-row")

def chart(transactions):
    return html.Div([
        html.H2("Transaction History"),
        html.Div([
            html.Div("Product Name", className="cell"),
            html.Div("Order Amount", className="cell"),
            html.Div("Date", className="cell"),
            html.Div("Type", className="cell")
        ], className="transactions-header"),
        html.Div(
            children=[entry(transaction) for _, transaction in transactions.iterrows()],
            className="transaction-list"
        )
    ], className="glass-card-transaction")


