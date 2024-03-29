from . import score_distribution_chart
from dash import Dash, html
import pandas as pd

from . import win_distribution_chart
from . import basic_stats
from . import score_boxplot

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    """
    The render function for overview feature.

    Args:
        app (Dash): The dash app.
        data (pd.DataFrame): The scrabble data.

    Returns:
        html.Div: Container for the overview feature.
    """
    return html.Div(
        className='grid-container',
        children=[
            html.Div(
                className='grid-item',
                children=[
                    win_distribution_chart.render(app, data)
                ]
            ),
            html.Div(
                className='grid-item',
                children=[
                    score_distribution_chart.render(app, data)
                ]
            ),
            html.Div(
                className='grid-item',
                children=[
                    basic_stats.render(app, data)
                ]
            ),
            html.Div(
                className='grid-item',
                children=[
                    score_boxplot.render(app, data)
                ]
            )
        ]
    )