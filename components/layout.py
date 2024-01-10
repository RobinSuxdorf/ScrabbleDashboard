from dash import Dash, dcc, html, Input, Output
import pandas as pd

from . import game_analysis

def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        children=[
            html.H1(app.title),
            html.Hr(),
            game_analysis.render(app, data)
        ]
    )