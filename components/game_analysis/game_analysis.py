from dash import Dash, dash_table, html
import plotly.express as px
import pandas as pd

from data.loader import DataSchema

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    """
    The render function for the game analysis feature.

    Args:
        app (Dash): The dash app.
        data (pd.DataFrame): The scrabble data.

    Returns:
        html.Div: Container for the game analysis feature.
    """
    filtered_data = data.dropna(subset=[DataSchema.DENIZ_SCORES, DataSchema.DANYEL_SCORES, DataSchema.ROBIN_SCORES])

    return html.Div(
        children=[
            dash_table.DataTable(
                id='game_analysis_table',
                data=filtered_data.to_dict('records'),
                columns=[
                    {"name": i, "id": i} for i in filtered_data.columns 
                    if i not in [DataSchema.DENIZ_SCORES, DataSchema.DANYEL_SCORES, DataSchema.ROBIN_SCORES]
                ],
                row_selectable='single',
                selected_rows=[0]
            ),
            html.Div(id='game_process_graph')
        ]
    )
    