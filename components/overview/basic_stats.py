from typing import Any
from dash import Dash, html, dash_table
import pandas as pd
from data.loader import DataSchema

def calculate_stats(data: pd.DataFrame) -> list[dict[str, Any]]:
    """
    Function for calculating some statistics from the scrabbel dataset.

    Args:
        data (pd.DataFrame): The scrabble data.

    Returns:
    list[dict[str, Any]]: List of rows containing a name for the statistics and the values for the individual player.
    """
    players = [DataSchema.DENIZ, DataSchema.DANYEL, DataSchema.ROBIN]

    stats: list[dict[str, Any]] = []

    df_temp = pd.DataFrame({player: data.apply(lambda row: row[players].max() - row[player], axis=1) for player in players})

    stats.append({
        'Statistik': 'Maximum',
        **data[players].max().to_dict()
    })

    stats.append({
        'Statistik': 'Minimum',
        **data[players].min().to_dict()
    })

    stats.append({
        'Statistik': 'Anzahl Spiele mit >= 200 Punkten',
        **data[players].apply(lambda row: (row >= 200).sum(), axis=0).to_dict()
    })

    stats.append({
        'Statistik': 'Anzahl Spiele mit < 100 Punkten',
        **data[players].apply(lambda row: (row < 100).sum(), axis=0).to_dict()
    })

    df_temp = (df_temp[players] > 0) & (df_temp[players] <= 5)
    stats.append({
        'Statistik': 'Knappe Niederlagen',
        **df_temp.sum().to_dict()
    })

    stats.append({
        'Statistik': 'Siege mit >= 50 Punkten abstand',
        **data[players].apply(lambda row: (row - data[players].drop(columns=row.name).max(axis=1)) >= 50).sum().to_dict()
    })

    return stats

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    """
    The render function for the basic_stats table.

    Args:
        app (Dash): The dash app.
        data (pd.DataFrame): The scrabble data.

    Returns:
        html.Div: Div containing the basic stats table.
    """
    return html.Div(
        children=[
            dash_table.DataTable(
                data=calculate_stats(data)
            )
        ]
    )