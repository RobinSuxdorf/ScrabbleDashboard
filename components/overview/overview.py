from . import score_distribution_chart
from dash import Dash, html
import pandas as pd

from . import win_distribution_chart
from . import basic_stats
from . import score_boxplot

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        children=[
            win_distribution_chart.render(app, data),
            score_distribution_chart.render(app, data),
            basic_stats.render(app, data),
            score_boxplot.render(app, data)
        ]
    )