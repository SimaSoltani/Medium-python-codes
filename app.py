# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 10:08:54 2020

@author: Sima
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


color = {
    'background':'#F0F8FF',
    'text':'#00008B'}


# assume you ahve a long form data frame
# see https://ployly.com/python/px-arguments/ for more options
df = pd.read_csv('data\\time_series_plotly.csv')

