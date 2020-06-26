#!/usr/bin/env python
# coding: utf-8

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.figure_factory as ff
import plotly.graph_objs as go
import plotly.offline as py
import plotly.express as px

from pandas import *
import pandas as pd
import numpy as np

stats1820 = pd.read_excel('all_stats.xlsx', sheet_name='stats1820')


franchises = stats1820['TEAM'].str.split(' ', n = 1, expand = True)
stats1820['Franchise'] = franchises[1]

hustle_and_oppblk = stats1820[['TEAM', 'Franchise',
                               'Screen  Assists','Screen  Assists PTS','Deflections','OFF Loose Balls  Recovered','DEF Loose Balls  Recovered',
                               'Loose Balls  Recovered','Charges  Drawn','Contested 2PT Shots','Contested 3PT Shots','Contested  Shots',
                               'deflection_rate','loose_ball_recover_rate','charges_drawn_rate','contest_rate','contested_2pt_rate',
                               'contested_3pt_rate','+/-', 'BLKA', 'OffRtg', 'DefRtg', 'NetRtg']]

col_options = [dict(label=x, value=x) for x in hustle_and_oppblk.columns]
dimensions = ['x', 'y', 'color']

app = dash.Dash(
    __name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
)

app.layout = html.Div(
    [
        html.H3('NBA Hustle and Team Performance Statistics (2018-2020 Season Pre COVID Suspension)'),
        html.Div(
            [
                html.P([d + ':', dcc.Dropdown(id=d, options=col_options)])
                for d in dimensions
            ],
            style={"width": "20%", "float": "left"},
        ),
        dcc.Graph(id="graph", style={'height': '95vh',"width": "75%", "display": "inline-block"}),
    ]
)


@app.callback(Output("graph", "figure"), [Input(d, "value") for d in dimensions])
def make_figure(x, y, color):
    return px.scatter(
        hustle_and_oppblk,
        x=x,
        y=y,
        color=color,
    )


app.run_server(debug=True)