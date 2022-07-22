from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

#Run with:
# py -m pytest --remote -k task5.py

dataset = pd.read_csv('data/pinkMorselSales.csv')
app = Dash(__name__)

app.layout = html.Div([
    html.Div(    
        html.Header(id='Header', children='Morsel Sales Page', style={"margin": "auto", "text-align": "center", "color": "#FFFFFF", "font-size": "50px"})
    ),
    html.Div(    
        dcc.RadioItems(
        ['All', 'North', 'South', 'East', 'West'],
        'All',
        id='Select-Region'
    ), style={"margin": "auto", "text-align": "center", "color": "#FFFFFF", "font-size": "25px"}),
    html.Div(
        dcc.Graph(
            id='Morsel-Sales',
            figure = px.line(dataset, x='date', y='sales', title='Pink Morsel Revenue Before And After 15/1/2021 Price Increase', labels={
                'date': 'Date',
                'sales': 'Net Revenue (Sales)'
            },
            )
        )
    )

], style={ "background-color": "#00AAFF", "width": "40%", "align-self": "center", "justify-content": "center"})

def test_bsly001_main(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_page(url=None, timeout=10)

    #Visualisation Present
    dash_duo.wait_for_element('#Morsel-Sales', timeout = 5)

    #Header Present
    dash_duo.wait_for_element('#Header', timeout = 5)

    #Radio Selection Present
    dash_duo.wait_for_element('#Select-Region', timeout = 5)