from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

dataset = pd.read_csv('data/pinkMorselSales.csv')

app = Dash(__name__)

app.layout = html.Div([
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

@app.callback(
    Output(component_id='Morsel-Sales', component_property='figure'),
    Input(component_id='Select-Region', component_property='value')
)
def set_region(selected_region):
    filtered_dataset = dataset if selected_region == "All" else dataset.query("region == '" + str(selected_region).lower() + "'")
    figure = px.line(filtered_dataset, x='date', y='sales', title='Pink Morsel Revenue Before And After 15/1/2021 Price Increase', 
        width=800, height=500,
        labels={
                'date': 'Date',
                'sales': 'Net Revenue (Sales)'
    })
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)