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


colors = {
    'background':'#F0F8FF',
    'text':'#00008B'}


# assume you ahve a long form data frame
# see https://ployly.com/python/px-arguments/ for more options
df = pd.read_csv('data\\time_series_plotly.csv')


from plotly.offline import plot
fig = px.scatter(df,x = 'Case_Reported_Date', y = 'Confirmed_cases', color = 'Reporting_PHU_City')
fig.update_traces(mode = 'markers+lines')
fig.update_layout(
    plot_bgcolor = colors['background'],
    paper_bgcolor = colors['background'],
    font_color = colors['text']
    )


markdown_text = '''
### ontario COVID 19 Dashboard

Creator : Sima

This is my first interactive dashboard using DASH
source of data: 
    
    
'''

app.layout = html.Div([
    dcc.Markdown(children = markdown_text,
                 style = {
                     'backgroundColor': colors['background'],
                     'textAlign':'center',
                     'color':colors['text']
                     }),
    dcc.Graph(
        id = 'example-graph',
        figure = fig
        )
    ])

if __name__ == '__main__':
    app.run_server(debug = True)