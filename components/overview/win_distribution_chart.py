from dash import Dash, dcc,  html
import pandas as pd
import plotly.express as px

from data.loader import DataSchema
from ..global_stylings import styling

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    """
    The render function for the win distribution chart.

    Args:
        app (Dash): The dash app.
        data (pd.DataFrame): The scrabble data.

    Returns:
        html.Div: Div containing the win distribution chart.
    """
    win_counts = data[DataSchema.WINNER].value_counts()

    wins_df = pd.DataFrame(win_counts).reset_index()
    wins_df.columns = ['Spieler', 'Siege']

    wins_df['Spieler'] = pd.Categorical(wins_df['Spieler'], [DataSchema.DENIZ, DataSchema.DANYEL, DataSchema.ROBIN, 'Unentschieden'])
    wins_df = wins_df.sort_values(['Spieler'])

    return html.Div(
        children=[
            dcc.Graph(
                figure=px.bar(
                    wins_df, 
                    x='Spieler', 
                    y='Siege',
                    color='Spieler',
                    color_discrete_map=styling.COLOR_MAP,
                )
            )
        ]
    )