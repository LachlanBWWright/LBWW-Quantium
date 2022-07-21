from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

dataset = pd.read_csv('data/pinkMorselSales.csv')

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        id='Morsel-Sales',
        figure=px.line(dataset, x='date', y='sales', title='Pink Morsel Revenue Before And After 15/1/2021 Price Increase', labels={
            'date': 'Date',
            'sales': 'Net Revenue (Sales)'
        })
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)