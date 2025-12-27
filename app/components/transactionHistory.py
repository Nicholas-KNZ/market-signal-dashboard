from dash import html

def entry(transaction):
    return html.Div(
        [
            html.Div(transaction["Name"], className="cell name"),
            html.Div(transaction["Stückzahl"], className="cell amount"),
            html.Div(transaction["Kaufdatum"], className="cell date"),
            html.Div("Kauf", className="cell type buy"),
        ],
        className="transaction-row"
    )

def chart(transactions):
    return html.Div(
        [
            html.H4("Transaction History"),

            html.Div(
                [
                    html.Div("Product", className="cell header"),
                    html.Div("Amount", className="cell header"),
                    html.Div("Date", className="cell header"),
                    html.Div("Type", className="cell header"),
                ],
                className="transactions-header"
            ),

            html.Div(
                [entry(transaction) for _, transaction in transactions.iterrows()],
                className="transaction-list"
            ),
        ],
        className="glass-card-transaction"
    )
