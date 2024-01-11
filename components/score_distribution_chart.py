from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

from data.loader import DataSchema

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        children=[
            dcc.Graph(figure=px.histogram(data, x=[DataSchema.DENIZ, DataSchema.DANYEL, DataSchema.ROBIN], barmode='overlay'))
        ]
    )