import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import sqlite3
from sqlite3 import Error
from db_functions import get_from_db

# Daten holen
df = get_from_db("spritpreise.db")
print('DF :', df)

app = dash.Dash(__name__)

# das ist die erste Line die gezeichnet wird (von Tanksellen ID)
fig = go.Figure(go.Scatter(
    x=df['datetime'],
    y=df['preis'],
    line_shape='spline',
    name="Spritpreis <br> fg"
))

# das sind dann die anderen Line die gezeichnet werden (von Tanksellen ID)
# sollte später in einer Schleife gemacht werden
fig.add_trace(go.Scatter(
    x=df['zeit'],
    y=df['l_druck'],
    line_shape='spline',
    name='l_druck'))




# style all the traces
fig.update_traces(
    hoverinfo="name+x+y",
    line={"width": 0.9},
    marker={"size": 8},
    mode="lines",
    )



fig.update_layout(
    title='Tank-Preise (von Stephan) Preis/l in €',
    height=850,
    xaxis_tickformat='%H:%M<br>%d.%m.%Y'
)




app.layout = html.Div(children=[
    html.H1(children='Hello :-)'),

    html.Div(children=''' Dash: Stephan '''),

    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "Diesel", "value": "diesel"},
                     {"label": "Benzin E5", "value": "e5"},
                     {"label": "benzin E10", "value": "e10"}],
                 multi=False,
                 value="diesel",
                 style={'width': "40%"}
                 ),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])



if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8081)
