from dash import Dash, html
import pandas as pd

from . import win_distribution_chart

def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        children=[
            html.H1(app.title),
            html.Hr(),
            win_distribution_chart.render(app, data)
        ]
    )