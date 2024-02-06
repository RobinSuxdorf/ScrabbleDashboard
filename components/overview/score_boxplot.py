from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

from data.loader import DataSchema
def render(app: Dash, data: pd.DataFrame) -> html.Div:
    """
    The render function for the boxplot.

    Args:
        app (Dash): The dash app.
        data (pd.DataFrame): The scrabble data.

    Returns:
        html.Div: Div containing the boxplot chart.
    """
    return html.Div(
        children=[
            dcc.Graph(
                figure=px.box(
                    data,
                    x=[DataSchema.DENIZ, DataSchema.DANYEL, DataSchema.ROBIN]
                )
            )
        ]
    )