from . import score_distribution_chart
from dash import Dash, html
import pandas as pd

from . import win_distribution_chart

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        children=[
            win_distribution_chart.render(app, data),
            score_distribution_chart.render(app, data)
        ]
    )